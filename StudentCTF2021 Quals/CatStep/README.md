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

The Levi distance is calculated by the number of times of adding, removing, correcting characters to have a string of characters that is the same as the comparison string.

After this test case. I already have the number of characters of the string in the flag.

![image](https://user-images.githubusercontent.com/84057292/136729849-0ffc3360-6cc2-46b2-8573-88538f39f8d9.png)

This website said that I can make `POST` request instead submit on this website manually. So, I will code a script which can make `POST` request continuously to get the corect flag.

In short, this is the brute-force method.

## EXPLOIT

I use this code to determine the characters that will appear in the string.

Then, I use this code 
