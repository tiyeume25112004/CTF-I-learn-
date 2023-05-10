import string
a=string.ascii_lowercase
key=int(input("Nhap key: "))
plaintext=input("Nhap plaintext")
cyphertext=""
saveText=""
for i in plaintext:
    # timf index cua chu cai
    saveText=a.find(i)
    saveText=saveText+key
    if saveText >= len(a):
        saveText=saveText%len(a)
    else:
        saveText=saveText
    cyphertext+=a[saveText]
print(f"cypherText: {cyphertext}")
