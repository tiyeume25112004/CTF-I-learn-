import requests
url="http://206.189.112.129:32421/flag"
for i in range(1002):
   r=requests.get(url)
   if "HTB" in r.text:
      print(r.text)
      break
