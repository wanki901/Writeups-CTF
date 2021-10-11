import string
import requests

URL = "https://cat-step.disasm.me/"

def query(body):
    response = requests.post(URL, data=body)
    return response.text;

charUsed = []

for c in string.printable:
    body = {"flag": "spbctf{" + c + "}"}
    responsed = query(body)
    if '27' in responsed:
        charUsed.append(c)
        
print(charUsed)
                