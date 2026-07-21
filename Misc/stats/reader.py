import os
import struct
import time
import math
import psutil

class MemoryReader:
    def __init__(self, pid):
        self.pid = pid
        self.memoryFile = open(f"/proc/{pid}/mem", "rb")

    def read(self, address, size):
        try:
            self.memoryFile.seek(address)
            return self.memoryFile.read(size)
        except Exception:
            return None

    def readFloat(self, address):
        data = self.read(address, 4)
        return struct.unpack('<f', data)[0] if data else 0.0

    def readInt(self, address):
        data = self.read(address, 4)
        return struct.unpack('<i', data)[0] if data else 0

    def readPointer(self, address):
        data = self.read(address, 8)
        return struct.unpack('<Q', data)[0] if data else 0

def getBase(pid, module="GameAssembly.so"):
    try:
        with open(f"/proc/{pid}/maps", "r") as binary:
            for line in binary:
                if module in line:
                    return int(line.split("-")[0], 16)
    except:
        pass
    return 0

def resolvePointerChain(reader, baseAddress, staticRVA, offsets):
    try:
        pointer = reader.readPointer(baseAddress + staticRVA)
        for offset in offsets:
            pointer = reader.readPointer(pointer + offset)
        return pointer
    except:
        return 0

def main(pid, speed):
    staticRVA = 0x035F4968
    offsets = [0xB8, 0x10, 0x3B0]
    positionListOffset = 0x78
    arrayDataStart = 0x20
    vector3Length = 0x0C

    reader = MemoryReader(pid)
    baseAddress = getBase(pid)

    slotHistory = {}
    threshold = 0.5 # meters
    timeout = 3.0 # when is declared a ghost

    print(f"[*] Monitoring started for PID {pid}...")

    try:
        while True:
            CGameStatePointer = resolvePointerChain(reader, baseAddress, staticRVA, offsets)

            if CGameStatePointer == 0:
                print("[!] Waiting for valid game state...", end="\r")
                time.sleep(1)
                continue

            positionsList = reader.readPointer(CGameStatePointer + positionListOffset)
            if positionsList == 0:
                time.sleep(0.5)
                continue

            positionsListLength = reader.readInt(positionsList + 0x18)

            os.system('cls' if os.name == 'nt' else 'clear') # for live updating
            print("--- Live Player Positions (Base: {}) ---".format(hex(baseAddress)))

            currentTime = time.time()
            playerCount = 0

            for i in range(min(positionsListLength, 64)):
                dataAddress = positionsList + arrayDataStart + (i * vector3Length)
                x = reader.readFloat(dataAddress)
                y = reader.readFloat(dataAddress + 0x04)
                z = reader.readFloat(dataAddress + 0x08)

                if x == 0.0 and y == 0.0 and z == 0.0:
                    continue # empty values = no memory there

                currentPosition = (x, y, z)

                if i not in slotHistory:
                    slotHistory[i] = {'position': currentPosition, 'lastMoveTime': currentTime}

                lastPosition = slotHistory[i]['position']
                distance = math.sqrt((x - lastPosition[0])**2 + (y - lastPosition[1])**2 + (z - lastPosition[2])**2) # literally just the 3D distance formula

                if distance > threshold:
                    slotHistory[i]['lastMoveTime'] = currentTime
                    slotHistory[i]['position'] = currentPosition

                if currentTime - slotHistory[i]['lastMoveTime'] > timeout:
                    continue

                print("{:02d} | X: {:8.2f} | Y: {:8.2f} | Z: {:8.2f}".format(i, x, y, z))
                playerCount += 1

            print("\n[*] Active moving players: {}".format(playerCount))
            time.sleep(1/speed)

    except KeyboardInterrupt:
        print("\n[*] Stopped.")
    finally:
        reader.memoryFile.close()

if __name__ == "__main__":
    target = ""
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == target:
            targetPID = proc.info['pid']
    main(pid=targetPID, speed=165)