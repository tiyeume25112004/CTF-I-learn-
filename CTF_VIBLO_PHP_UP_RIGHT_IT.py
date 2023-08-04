import requests
url="http://172.104.49.143:1335/"
y=""
z=""
while True:
    r=requests.get(url+y,allow_redirects=False,cookies={"PHPSESSID":"45fa471cada9ed85fe4211452a5b62b1"})
    y=r.headers['location']
    z+=y
    print(z.replace("?",""))
#nó stuck một vài chỗ, chạy vài lần là đc
