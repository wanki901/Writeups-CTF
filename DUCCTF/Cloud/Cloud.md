# CHALLENGE NAME: Bad Bucket

## DESCRIPTION

Aw yea have you guys SEEN my new website... its nearly done I swear! I've uploaded it to the ☁️CLOUD☁️ and shared it with you guys now so you can see it! Check it out here

## ATTACHMENT

[https://storage.googleapis.com/the-bad-bucket-ductf/index.html](https://storage.googleapis.com/the-bad-bucket-ductf/index.html)

##SOLUTION

Go to the web site in the attachment but nothing special here.

![image](https://user-images.githubusercontent.com/84057292/134917500-21bd49c4-c78a-4be1-884c-23c10a0418f3.png)

I tried to delete `index.html` in the URL so I got this.

<p align = center>
  <img src="https://user-images.githubusercontent.com/84057292/134918550-732d9a11-7567-4b44-8f62-3953d5211b03.png">
</p>

I found `buckets/.notaflag` have a pretty similar structure to `index.html` and other images, so I tried replacing `buckets/.notaflag` with `index.html`. And I got the flag.

![image](https://user-images.githubusercontent.com/84057292/134919321-da2b1090-839f-4a3b-acbc-35709db38997.png)

## FLAG

`DUCTF{if_you_are_beggining_your_cloud_journey_goodluck!}`


