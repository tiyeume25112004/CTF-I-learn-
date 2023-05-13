from pwn import *
r=remote("static-01.heroctf.fr",8000)
r.recvline()
while True:
    string=r.recv()
    print(string)
    string=eval(string.decode().replace("=",""))
    print(string)
    string=bytes(str(string),"utf-8")
    r.sendline(string)
