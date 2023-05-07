from operator import xor
string = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
string_ord=[o for o in bytes.fromhex(string)]
print(string_ord)
for i in range(256):
    posible_flag=[i^u for u in string_ord]
    s="".join([chr(u) for u in posible_flag ])
    if s.startswith("crypto"):
        print(s)
