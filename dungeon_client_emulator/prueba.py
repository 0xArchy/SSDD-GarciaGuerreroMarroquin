#!/usr/bin/python3
from makeelf.elf import *
fd = os.open('dungeon_client_emulator', os.O_RDONLY)
b = os.read(fd, 0xffff)
os.close(fd)

elf, b = Elf32.from_bytes(b)
print(elf)
