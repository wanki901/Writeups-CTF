# CHALLENGE NAME: CatStep

## CATEGORY: PPC

## DESCRIPTION

Greeting human!

We want to play a game with you. The mission is simple: you need to guess our flag, that’s all. We use an algorithm to determine the similarity of strings.

## ATTACHMENT

Website: [cat-step.disasm.me/](https://cat-step.disasm.me/)

## METHODOLOGY

Go to this website, we will see how to beat this challenge.

![image](https://user-images.githubusercontent.com/84057292/136728468-083ff803-d63b-4e26-8337-e2e43b4cee20.png)

After learning the Levenshtein distance, I came up with: 

The Levenshtein distance is calculated by the number of times of adding, removing, correcting characters to have a string of characters that is the same as the comparison string.

After this test case. I already have the number of characters of the string in the flag.

![image](https://user-images.githubusercontent.com/84057292/136729849-0ffc3360-6cc2-46b2-8573-88538f39f8d9.png)

This website said that I can make `POST` request instead submit on this website manually. So, I will code a script which can make `POST` request continuously to get the corect flag.

In short, this is the brute-force method.

## EXPLOIT

I use this code to determine the characters that will appear in the string.

```python
import string
import requests                               #import library for sending request

URL = "https://cat-step.disasm.me/"

def query(body):                              #sending request and recieve responce
    response = requests.post(URL, data=body)
    return response.text;

charUsed = []

for c in string.printable:                    #test all printable characters 
    body = {"flag": "spbctf{" + c + "}"}      #request
    responsed = query(body)
    if '27' in responsed:                     #if this character appear in flag, the Levenshtein distance will drop to 27
        charUsed.append(c)
        
print(charUsed)
```

I have obtained the characters that will appear in the string in the flag

![image](https://user-images.githubusercontent.com/84057292/136746178-21db111b-6328-4742-8539-a61f30ee0e5c.png)


Then, I use this code to detect the characters one by one and put them in the string to complete the flag.

```python
import string
import requests

URL = "https://cat-step.disasm.me"

def query(body):
    r = requests.post(URL, data=body)
    return r.text

#All characters will appear in string in flag
charUsed = ['0', '5', 'a', 'b', 'c', 'e', 'f', 'g', 'i', 'n', 's', 't', 'u', 'w', 'y', 'z', 'A', 'F', 'G', 'O', 'S', '_'] 

Levenshtein_distance = 28   
flag = list("spbctf{rrrrrrrrrrrrrrrrrrrrrrrrrrrr}")             #format of flag, I use characters "r" because it doesn't in charUsed

#Get each element in charUsed in turn replacing each position in the string "rrr...rrr"
for i in charUsed:
    for j in range(7,35):
        #if j not in _index:
            pre_flag = ''.join(flag)
            flag[j] = i
            body = {"flag": ''.join(flag)}
            responsed = query(body)
            if str(Levenshtein_distance - 1) not in responsed:  #check if this character is correct
                flag = list(pre_flag)
            else:
                Levenshtein_distance -= 1

print(''.join(flag))
```

I got the flag.

![image](https://user-images.githubusercontent.com/84057292/136745209-02daee2a-5d27-4139-ae14-4f82d1b2a5f1.png)

## FLAG 

`spbctf{easy_web_fuzzing_0t5AFzSG0Oc}`
