from hashlib import md5
for i in range(1,10000000):
  if md5(str(i).encode("UTF-8")).hexdigest()[:6]=="6d0bc1":
    print(i)
