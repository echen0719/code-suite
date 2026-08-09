import os
import struct
import time
import math
from values import commonValues, CGameStateValues, webguyValues

class MemoryReader:
    def __init__(self, pid):
        self.pid = pid
        self.memoryFile = os.open(f"/proc/{pid}/mem", os.O_RDONLY)

        self.baseAddress = self.getBase()
        self.webguyBase = 0
        self.CGameStateBase = 0

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
        pointer = self.readPointer(self.baseAddress + CGameStateValues["staticRVA"])
        if pointer:
            for offset in CGameStateValues["offsets"]:
                pointer = self.readPointer(pointer + offset)
                if not pointer: break
        self.CGameStateBase = pointer

        pointer = self.readPointer(self.baseAddress + webguyValues["staticRVA"])
        if pointer:
            for offset in webguyValues["offsets"]:
                pointer = self.readPointer(pointer + offset)
                if not pointer: break
        self.webguyBase = pointer

    def getPlayers(self):
        if not self.CGameStateBase or not self.webguyBase: return []

        # positions
        positionPointer = self.readPointer(self.CGameStateBase + CGameStateValues["positionOffset"])
        if not positionPointer: return []

        positionArrayLength = self.readInt(positionPointer + commonValues["arrayLengthOffset"]) if positionPointer else self.maxPlayerCount
        positionData = self.read(positionPointer + commonValues["arrayStartOffset"], positionArrayLength * self.vector3Length)

        # visibility
        visiblePointer = self.readPointer(self.webguyBase + webguyValues["visibleListOffset"])
        if not visiblePointer: return []

        visibleArrayLength = self.readInt(visiblePointer + commonValues["arrayLengthOffset"]) if visiblePointer else self.maxPlayerCount
        visibleData = self.read(visiblePointer + commonValues["arrayStartOffset"], visibleArrayLength)

        positions = struct.unpack('<{}f'.format(positionArrayLength * 3), positionData)
        visibles = struct.unpack('<{}B'.format(visibleArrayLength), visibleData)

        currentTime = time.time()
        activePlayers = []

        for i in range(min(positionArrayLength, visibleArrayLength, self.maxPlayerCount)):
            x, y, z = positions[i * 3], positions[i * 3 + 1], positions[i * 3 + 2]
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

            activePlayers.append({'id': i, 'x': x, 'y': y, 'z': z, 'visible': visibles[i] != 0})

        return activePlayers

    def getCameraInfo(self):
        if not self.CGameStateBase: return None

        # viewPos - 0x18, viewOrient - 0x24, viewOrient end = 0x30, 0x30 - 0x24 = 24
        cameraCoordinates = self.read(self.CGameStateBase + CGameStateValues["cameraPositionOffset"], self.vector3Length)
        cameraOrientation = self.read(self.CGameStateBase + CGameStateValues["cameraOrientationOffset"], self.vector3Length)

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