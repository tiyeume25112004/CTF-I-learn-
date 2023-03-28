from operator import xor
a=["f",0x0A,"k",0x0C,"w","&","O",".","@",0x11,"x",0x0D,"Z",";","U",0x11,"p",0x19,"F",0x1F,"v",'"',"M","#","D",0x0E,"g",6,"h",0x0F,"G","2","O",]
# print(chr(xor(ord("f"),10))) -->l
print(len(a))
x="f"
for i in range(1,len(a)):
    if(isinstance(a[i],int)):
        if(isinstance(a[i-1],str)):
           x+=chr(xor(ord(a[i-1]),a[i]))
        if(isinstance(a[i-1],int)):
           x+=chr(xor(a[i-1],a[i]))
    if(isinstance(a[i],str)):
       if(isinstance(a[i-1],int)):
            x+=chr(xor(a[i-1],ord(a[i])))
       if(isinstance(a[i-1],str)):
            x+=chr(xor(ord(a[i-1]),ord(a[i])))
print(x)
print(len(x))
