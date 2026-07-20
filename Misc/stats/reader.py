import os
import struct
import time
import math

class MemoryReader:
    def __init__(self, pid):
        self.pid = pid
        self.mem_file = open(f"/proc/{pid}/mem", "rb")

    def read(self, address, size):
        try:
            self.mem_file.seek(address)
            return self.mem_file.read(size)
        except Exception:
            return None

    def read_float(self, address):
        data = self.read(address, 4)
        return struct.unpack('<f', data)[0] if data else 0.0

    def read_int(self, address):
        data = self.read(address, 4)
        return struct.unpack('<i', data)[0] if data else 0

    def read_pointer(self, address):
        data = self.read(address, 8)
        return struct.unpack('<Q', data)[0] if data else 0

def get_base_address(pid, module_name="GameAssembly.so"):
    try:
        with open(f"/proc/{pid}/maps", "r") as f:
            for line in f:
                if module_name in line:
                    return int(line.split("-")[0], 16)
    except: pass
    return 0

def resolve_pointer_chain(reader, base_addr, static_rva, offsets):
    try:
        ptr = reader.read_pointer(base_addr + static_rva)
        for offset in offsets:
            ptr = reader.read_pointer(ptr + offset)
        return ptr
    except: return 0

def main():
    pid = 20018
    STATIC_RVA = 0x03735438
    POINTER_OFFSETS = [0x80, 0x550, 0x3B0]
    POS_LIST_OFFSET = 0x78
    ARRAY_DATA_START = 0x20
    VECTOR3_STRIDE = 0x0C

    reader = MemoryReader(pid)
    base_addr = get_base_address(pid)

    slot_history = {}
    MOVE_THRESHOLD = 0.5
    GHOST_TIMEOUT = 3.0

    print(f"[*] Monitoring started for PID {pid}...")

    try:
        while True:
            cgamestate_ptr = resolve_pointer_chain(reader, base_addr, STATIC_RVA, POINTER_OFFSETS)

            if cgamestate_ptr == 0:
                print("[!] Waiting for valid game state...", end="\r")
                time.sleep(1)
                continue

            pos_list_array = reader.read_pointer(cgamestate_ptr + POS_LIST_OFFSET)
            if pos_list_array == 0:
                time.sleep(0.5)
                continue

            array_length = reader.read_int(pos_list_array + 0x18)

            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"--- Live Player Positions (Base: {hex(base_addr)}) ---")

            current_time = time.time()
            active_players = 0

            for i in range(min(array_length, 64)):
                base_data_addr = pos_list_array + ARRAY_DATA_START + (i * VECTOR3_STRIDE)
                x = reader.read_float(base_data_addr)
                y = reader.read_float(base_data_addr + 0x04)
                z = reader.read_float(base_data_addr + 0x08)

                if x == 0.0 and y == 0.0 and z == 0.0:
                    continue

                current_pos = (x, y, z)

                if i not in slot_history:
                    slot_history[i] = {'pos': current_pos, 'last_move_time': current_time}

                last_pos = slot_history[i]['pos']
                dist = math.sqrt((x - last_pos[0])**2 + (y - last_pos[1])**2 + (z - last_pos[2])**2)

                if dist > MOVE_THRESHOLD:
                    slot_history[i]['last_move_time'] = current_time
                    slot_history[i]['pos'] = current_pos

                if current_time - slot_history[i]['last_move_time'] > GHOST_TIMEOUT:
                    continue

                print(f"{i:02d} | X: {x:8.2f} | Y: {y:8.2f} | Z: {z:8.2f}")
                active_players += 1

            print(f"\n[*] Active moving players: {active_players}")
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("\n[*] Stopped.")
    finally:
        reader.mem_file.close()

if __name__ == "__main__":
    main()