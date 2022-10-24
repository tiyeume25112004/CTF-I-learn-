import requests
def find(page):
    url="http://34.76.206.46:10008/"
    params={
        "page":page
    }
    r=requests.get(url,params=params)
    output=f"{page} has word{r.text}"
    return output
for i in range(500):
    x=find(i)
    y=find(i)
    if(x==y):
        print(x)
# Để ý rằng khi các trang 1,2,3 load thì các từ không đổi nên tui code 1 đoạn python lấy ra ký tự, xem quy luật như nào :V
# do tui không biết dãy fo nên tui hỏi thk bạn và được nó nói UwU cho biết. Đoạn fobinacci lười quá tự làm đi
