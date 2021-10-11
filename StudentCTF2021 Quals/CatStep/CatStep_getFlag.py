import string
import requests

URL = "https://cat-step.disasm.me"

def query(body):
    r = requests.post(URL, data=body)
    return r.text

charUsed = ['0', '5', 'a', 'b', 'c', 'e', 'f', 'g', 'i', 'n', 's', 't', 'u', 'w', 'y', 'z', 'A', 'F', 'G', 'O', 'S', '_']
Levenshtein_distance = 28
flag = list("spbctf{rrrrrrrrrrrrrrrrrrrrrrrrrrrr}")
for i in charUsed:
    for j in range(7,35):
        pre_flag = ''.join(flag)
        flag[j] = i
        body = {"flag": ''.join(flag)}
        responsed = query(body)
        if str(Levenshtein_distance - 1) not in responsed:
            flag = list(pre_flag)
        else:
            Levenshtein_distance -= 1
        if Levenshtein_distance == 0:
            break
    if Levenshtein_distance == 0:
        break
    
print(''.join(flag))