ihl_version = 0x45
print(hex(ihl_version >> 4))   # 0x4 — версия
print(hex(ihl_version & 0xF))  # 0x5 — IHL
print(ihl_version)    
