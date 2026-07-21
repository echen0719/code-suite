import os
import struct
import time
import math
from offsets import values

class MemoryReader:
    def __init__(self, pid):
        self.pid = pid
        self.memoryFile = open(f"/proc/{pid}/mem", "rb")
        self.baseAddress = self.getBase()

        self.staticRVA = values['staticRVA']
        self.offsets = values['offsets']

        self.positionOffset = values['positionOffset']
        self.arrayDataStart = values['arrayDataStartOffset']
        self.cameraPositionOffset = values['cameraPositionOffset']
        self.cameraOrientationOffset = values['cameraOrientationOffset']

        self.arrayDataLengthOffset = values['arrayDataLengthOffset']
        self.vector3Length = 0xC # 12 bytes

        self.slotHistory = {}
        self.threshold = 0.5 # meters
        self.timeout = 3.0 # when is declared a ghost

    def read(self, address, size):
        try:
            self.memoryFile.seek(address)
            return self.memoryFile.read(size)
        except Exception:
            return None

    # convert 4 bytes to float
    def readFloat(self, address):
        data = self.read(address, 4)
        return struct.unpack('<f', data)[0] if data else 0.0

    # convert 4 bytes to int
    def readInt(self, address):
        data = self.read(address, 4)
        return struct.unpack('<i', data)[0] if data else 0

    # convert 8 bytes to 64-bit pointer
    def readPointer(self, address):
        data = self.read(address, 8)
        return struct.unpack('<Q', data)[0] if data else 0

    def getBase(self, module="GameAssembly.so"):
        try:
            with open(f"/proc/{self.pid}/maps", "r") as binary:
                for line in binary:
                    if module in line:
                        return int(line.split("-")[0], 16)
        except:
            pass
        return 0

    def resolvePointerChain(self, baseAddress, staticRVA, offsets):
        try:
            pointer = self.readPointer(baseAddress + staticRVA)
            for offset in offsets:
                pointer = self.readPointer(pointer + offset)
            return pointer
        except:
            return 0

    def getPlayers(self):
        CGameStatePointer = self.resolvePointerChain(self.baseAddress, self.staticRVA, self.offsets)
        if CGameStatePointer == 0:
            return []

        positionsList = self.readPointer(CGameStatePointer + self.positionOffset)
        if positionsList == 0:
            return []

        positionsListLength = self.readInt(positionsList + self.arrayDataLengthOffset)
        currentTime = time.time()
        activePlayers = []

        for i in range(min(positionsListLength, 64)):
            dataAddress = positionsList + self.arrayDataStart + (i * self.vector3Length)

            coordinates = self.read(dataAddress, 12)
            # read 12 bytes then unpack
            if not coordinates or len(coordinates) < 12:
                continue

            x, y, z = struct.unpack('<fff', coordinates)
            if x == 0.0 and y == 0.0 and z == 0.0:
                continue # empty values = no memory there

            currentPosition = (x, y, z)

            if i not in self.slotHistory:
                self.slotHistory[i] = {'position': currentPosition, 'lastMoveTime': currentTime}

            lastPosition = self.slotHistory[i]['position']
            distance = math.sqrt((x - lastPosition[0])**2 + (y - lastPosition[1])**2 + (z - lastPosition[2])**2) # literally just the 3D distance formula

            if distance > self.threshold:
                self.slotHistory[i]['lastMoveTime'] = currentTime
                self.slotHistory[i]['position'] = currentPosition

            if currentTime - self.slotHistory[i]['lastMoveTime'] > self.timeout:
                continue

            activePlayers.append({
                'id': i, 'x': x, 'y': y, 'z': z
            })
        return activePlayers

    def getCameraInfo(self):
        CGameStatePointer = self.resolvePointerChain(self.baseAddress, self.staticRVA, self.offsets)
        if CGameStatePointer == 0:
            return []

        # viewPos - 0x18
        cameraPositionDataAddress = CGameStatePointer + self.cameraPositionOffset
        cameraCoordinates = self.read(cameraPositionDataAddress, 12)

        if not cameraCoordinates or len(cameraCoordinates) < 12:
            return []

        cameraX, cameraY, cameraZ = struct.unpack('<fff', cameraCoordinates)
        if cameraX == 0.0 and cameraY == 0.0 and cameraZ == 0.0:
            return []

        # viewOrient - 0x24 (Euler angles)
        cameraOrientationDataAddress = CGameStatePointer + self.cameraOrientationOffset
        cameraOrientations = self.read(cameraOrientationDataAddress, 12)

        if not cameraOrientations or len(cameraOrientations) < 12:
            return []

        pitch, yaw, roll = struct.unpack('<fff', cameraOrientations)
        if pitch == 0.0 and yaw == 0.0 and roll == 0.0:
            return []

        return {
            'x': cameraX, 'y': cameraY, 'z': cameraZ,
            'pitch': math.radians(pitch),
            'yaw': math.radians(yaw),
            "roll": math.radians(roll)
        }

    def close(self):
        try:
            self.memoryFile.close()
        except Exception:
            pass