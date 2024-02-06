from pwn import *
def morse_to_text(morse_code):
    morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
        '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
        '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
        '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
        '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
        '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
        '.-.-.-': '.', '--..--': ',', '---...': ':', '-.-.-.': ';', '..--..': '?',
        '-....-': '-', '-..-.': '/', '.--.-.': '@', '...-..-': '$', '.----.': "'",
        '-.--.': '(', '-.--.-': ')', '.-...': '&', '---.': '!', '-.-.--': '!', '-.-.': 'C',
        '-...-': '=', '.-.-.': '+', '.-..-.': '"', '.--.-.': '@', '-.--.': '(',
        '-.--.-': ')', '-...-': '=', '.-.-.': '+', '.-..-.': '"', '.--.-.': '@'
    }

    morse_code = morse_code.strip()  # Remove leading/trailing whitespaces
    words = morse_code.split(' / ')
    decoded_message = ""

    for word in words:
        letters = word.split()
        for letter in letters:
            decoded_message += morse_code_dict.get(letter, '?')  # '?' for unknown characters
        decoded_message += ' '

    return decoded_message.strip()  # Remove trailing whitespace


r= remote("207.148.79.171",4000)
r.recvuntil("Question:")
try:
    while(True):
        string= r.recv().decode('utf-8').split("Answer")[0]
        print(string)
        payload = morse_to_text(string)
        r.sendline(bytes(str(payload),"utf-8"))
        print(r.recv())
except:
    print(r.recv())
r.interactive()
