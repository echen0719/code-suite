import os
import struct
import time
import math
from values import values

class MemoryReader:
    def __init__(self, pid):
        self.pid = pid
        self.memoryFile = os.open(f"/proc/{pid}/mem", os.O_RDONLY)
        self.baseAddress = self.getBase()

        self.staticRVA = values['staticRVA']
        self.offsets = values['offsets']

        self.positionOffset = values['positionOffset']
        self.arrayDataStart = values['arrayDataStartOffset']
        self.arrayDataLengthOffset = values['arrayDataLengthOffset']

        self.cameraPositionOffset = values['cameraPositionOffset']
        self.cameraOrientationOffset = values['cameraOrientationOffset']

        self.maxPlayerCount = 64
        self.vector3Length = 0xC # 12 bytes

        self.slotHistory = {}
        self.thresholdSQR = 0.25 # meters
        self.timeout = 3.0 # when is declared a ghost

    def read(self, address, size):
        try:
            return os.pread(self.memoryFile, size, address)
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

    def resolvePointerChain(self):
        try:
            pointer = self.readPointer(self.baseAddress + self.staticRVA)
            for offset in self.offsets:
                pointer = self.readPointer(pointer + offset)
            return pointer
        except:
            return 0

    def getPlayers(self):
        CGameStatePointer = self.resolvePointerChain()
        if not CGameStatePointer: return []

        positionsList = self.readPointer(CGameStatePointer + self.positionOffset)
        if not positionsList: return []

        # 64 max players all the time
        coordinates = self.read(positionsList + self.arrayDataStart, self.maxPlayerCount * self.vector3Length)
        if not coordinates or len(coordinates) < self.maxPlayerCount * self.vector3Length: return []

        floats = struct.unpack('<{}f'.format(self.maxPlayerCount * 3), coordinates)

        currentTime = time.time()
        activePlayers = []

        for i in range(self.maxPlayerCount):
            x, y, z = floats[i * 3], floats[i * 3 + 1], floats[i * 3 + 2]
            if x == 0.0 and y == 0.0 and z == 0.0:
                continue # empty values = no memory there

            currentPosition = (x, y, z)

            if i not in self.slotHistory:
                self.slotHistory[i] = {'position': currentPosition, 'lastMoveTime': currentTime}

            lastPosition = self.slotHistory[i]['position']
            distanceSQR = (x - lastPosition[0])**2 + (y - lastPosition[1])**2 + (z - lastPosition[2])**2 # literally just the 3D distance formula

            if distanceSQR > self.thresholdSQR:
                self.slotHistory[i]['lastMoveTime'] = currentTime
                self.slotHistory[i]['position'] = currentPosition

            if currentTime - self.slotHistory[i]['lastMoveTime'] > self.timeout:
                continue

            activePlayers.append({'id': i, 'x': x, 'y': y, 'z': z})

        return activePlayers

    def getCameraInfo(self):
        CGameStatePointer = self.resolvePointerChain()
        if not CGameStatePointer: return None

        # viewPos - 0x18, viewOrient - 0x24, viewOrient end = 0x30, 0x30 - 0x24 = 24
        cameraCoordinates = self.read(CGameStatePointer + self.cameraPositionOffset, self.vector3Length)
        cameraOrientation = self.read(CGameStatePointer + self.cameraOrientationOffset, self.vector3Length)

        if not cameraCoordinates or not cameraOrientation: return None

        cameraX, cameraY, cameraZ = struct.unpack('<fff', cameraCoordinates)
        pitch, yaw, roll = struct.unpack('<fff', cameraOrientation)

        if cameraX == 0.0 and cameraY == 0.0 and cameraZ == 0.0:
            return None
        if pitch == 0.0 and yaw == 0.0 and roll == 0.0:
            return None

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