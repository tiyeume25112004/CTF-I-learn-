import requests
import base64
url="http://misc.bbctf.fluxus.co.in:2002"
a='9'
for i in range(1,50):
    u=a*i
    print(u)
    data={"key_num":u}
    r=requests.post(url,data=data)
    b=r.text.split("</p>")[0].split("</b> ")
    print(base64.b64decode(b[1]))
    
# 999999999999999999999
# b'https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=195s'
# 21
# 9999999999999999999999
# b'https://www.youtube.com/watch?v=FIUbRJkKjlE' -> this is link, download video and decode morse or you can brute 1->99
# 22
# 99999999999999999999999
# b'https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=3s'
# 23
# 999999999999999999999999
# b'https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=39s
