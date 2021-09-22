# Challenge Name: MILKSLAP

## DESCRIPTION 

  An icon. When we click it, we will go to this site http://mercury.picoctf.net:48319/

  And we'll see a gif that has a man who was splashed milk by another one.

## PROBLEM

  Because this is an forensic challenge, not web so I think the flag will be hide in the gif. So, maybe our problem is stegnography.
  
## SOLUTION

I determine this problem is stegnography, so I need the gif.
Open the source page.

**Source code**

![This is a alt text.](https://cdn.discordapp.com/attachments/871393677304553473/889927694324744222/unknown.png "Source code.")

Nothing special. So, I check file `style.css`

![image](https://user-images.githubusercontent.com/84057292/134220858-237361af-bf7e-46c4-9eab-0c098bcbb865.png "style.css")

We've got the [gif](http://mercury.picoctf.net:48319/concat_v.png)'s link and we can get it.

After download it, use `zsteg` to check all stegnography algorithm that was supported.

![image](https://user-images.githubusercontent.com/84057292/134265693-8539b85e-1343-49b8-996d-06a06c003bae.png)

Ah, so we got flag.

Flag: `picoCTF{imag3_m4n1pul4t10n_sl4p5}`

