# coding:UTF-8

from pwn import *
context(os='linux',arch='amd64')

Debug=1
if Debug:
    io=process('./get_shell')
else:
    io=remote('???','???') # ����û�����߻���

def main():
    io.interactive()

main()