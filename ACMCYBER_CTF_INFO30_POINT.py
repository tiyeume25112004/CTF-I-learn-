import requests
from bs4 import BeautifulSoup
import math
import hashlib

url = "https://jester.acmcyber.com/"

page1 = requests.get(url)

print(page1.text)

soup = BeautifulSoup(page1.text, 'html.parser')

num1 = soup.find_all('p')[2].text.split(' ')[2]
num2 = soup.find_all('p')[2].text.split(' ')[4]

sum = int(num1) + int(num2)

page2 = requests.post(url + "validate", data={'answer':sum})

print(page2.text)

soup = BeautifulSoup(page2.text, 'html.parser')

a = soup.find_all('p')[1].text.split(' ')[5]
b = soup.find_all('p')[1].text.split(' ')[8]
c = soup.find_all('p')[1].text.split(' ')[11]

a = int(a)
b = int(b)
c = int(c)

ans1 = round((-1 * b + math.sqrt(b * b - 4 * a * c)) / (2 * a))
ans2 = round((-1 * b - math.sqrt(b * b - 4 * a * c)) / (2 * a))

cookies = {'part2': hashlib.sha256(b"True").hexdigest()}

page3 = requests.post(url + "validate", data={'answer1':ans1, 'answer2':ans2}, cookies=cookies)

print(a, b, c)
print(ans1, ans2)

print(page3.text)
