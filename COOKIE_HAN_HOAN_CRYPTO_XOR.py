text = "6c 46 4b 4d 51 4b 74 48 17 49 17 14 48 74 49 17 4b 57"
text= text.split(' ')
def decrypt(text,key):
    flag = ""
    for i in range (len(text)) :
        temp = chr(int(text[i],16) ^ ord(key[i%len(key)]))
        flag += temp
    return flag
for i in range(256):
    key =  chr(i)
    print(decrypt(text,key))
#collab voi Thanh :c t kem crypto v
