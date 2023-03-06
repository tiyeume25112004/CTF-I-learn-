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
