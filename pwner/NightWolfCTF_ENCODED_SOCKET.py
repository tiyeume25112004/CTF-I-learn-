from pwn import *
import binascii
import base64

def binaryConvert(binary_data):
    return ''.join([chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8)])
def base64Convert(base64_data):
    return base64.b64decode(base64_data).decode('utf-8')
def base32Convert(base32_data):
    return base64.b32decode(base32_data).decode('utf-8')
def base16Convert(base16_data):
    return bytes.fromhex(base16_data).decode('utf-8')
def base8Convert(base8_data):
    return ''.join([chr(int(base8_data[i:i+3], 8)) for i in range(0, len(base8_data), 3)])


r=remote("152.67.127.64",8025)
r.recvline()
for i in range(200):
    string=r.recv()
    string=string.decode().split("answer for ")[1].split("?")[0]
    choose=string.split(":")[0]
    hashes=string.split(":")[1]
    if(choose=="64"):
        r.sendline(bytes(str(base64Convert(hashes)),"utf-8"))
        string=r.recv()
        print(string)
    elif(choose=="2"):
        r.sendline(bytes(str(binaryConvert(hashes)),"utf-8"))
        string=r.recv()
        print(string)
    elif(choose=="32"):
        r.sendline(bytes(str(base32Convert(hashes)),"utf-8"))
        string=r.recv()
        print(string)
    elif(choose=="16"):
        r.sendline(bytes(str(base16Convert(hashes)),"utf-8"))
        string=r.recv()
        print(string)
    elif(choose=="8"):
        r.sendline(bytes(str(base8Convert(hashes)),"utf-8"))
        string=r.recv()
        print(string)
    else:
        print(r.recv())
r.interactive()
