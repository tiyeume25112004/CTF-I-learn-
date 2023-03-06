# i learned sent data with pwntools
from pwn import *
import re
import string

#context.log_level = "DEBUG"

r = remote("2019shell1.picoctf.com", 7380)

def get_base_encoded_str(r):
    s = r.recvuntil("the ")
    if ("Please" not in s):
        r.recvline()
        return None
    s = r.recvuntil(" as a word.", drop = True)
    return s.strip()

def decode_string_as_char_array(s, base):
    res = ""
    for unit in s.split(" "):
        c = chr(int(unit, base))
        if c not in string.ascii_letters:
            raise Exception("Non-ASCII result")
        res += c
    return res

def try_decode_as_char_array_with_unknown_base(s):
    for base in range(1, 17):
        try:
            res = decode_string_as_char_array(s, base)
            log.info("Decode successful with base {}".format(base))
            return res
        except:
            pass
    return None

def try_decode_as_hex(s):
    try:
        return s.decode("hex")
    except:
        return None

r.recvline()
r.recvline()
s = get_base_encoded_str(r)
while s is not None:
    log.info("Trying to decode '{}'".format(s))
    res = try_decode_as_char_array_with_unknown_base(s) or try_decode_as_hex(s)
    if res is None:
        log.error("Can't decode '{}'".format(s))
        break
    log.info("Decoded as '{}'".format(res))
    r.sendlineafter("Input:", res)
    s = get_base_encoded_str(r)

print r.recvall()
"""
from pwn import *

sh = remote('2019shell1.picoctf.com', 20836)

binary_data = sh.recvuntil('Input:\n').split('\n')[2].split(' ')[3:-3]
binary_data = ''.join(map(lambda x: chr(int(x, 2)), binary_data))
sh.sendline(binary_data)

oct_data = sh.recvuntil('Input:\n').split('\n')[0].split('the  ')[-1].split(' as')[0].split(' ')
oct_data = ''.join(map(lambda x: chr(int(x, 8)), oct_data))
sh.sendline(oct_data)

hex_data = sh.recvuntil('Input:\n').split('\n')[0].split('the ')[-1].split(' as')[0]
hex_data = hex_data.decode('hex')
sh.sendline(hex_data)

sh.interactive()
"""
