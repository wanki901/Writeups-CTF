# CHALLENGE NAME: Who goes there?

## DESCRIPTION

Disclaimer: Please note that this storyline, including any previous or future additions are all fictional and created solely for this challenge as part of DownUnder CTF. These are real places however they have no association/affiliation to the event, you are not required to call any place or make contact with anyone, doing so may disqualify you from the event.

Welcome to the team, glad you chose to join us - hopefully you’ll like it here and want to stay. Let me tell you about your first task:

We’ve observed an underground criminal RaaS operation calling back to this domain, can you find the number of the individual who registered the domain?

`Flag format is DUCTF{+61<number>}`

## ATTACHMENT

A website with domain: [646f776e756e646572.xyz](646f776e756e646572.xyz)

## SOLUTION

I visited the website but it's nothing special. So I used some framework that allows me to check website registration information called [Who.is](https://who.is/) or [MarkMonitor Whois Search](https://whois-webform.markmonitor.com/whois/).

![image](https://user-images.githubusercontent.com/84057292/134809052-b93fa82d-a9d5-4cff-8bc9-a969d81d7ee9.png "Who.is")

<p align = center> Who.is </p>

![image](https://user-images.githubusercontent.com/84057292/134809370-12b68a0d-dde5-48b4-a4b0-f7d2104c04ab.png "MarkMonitor Whois Search")

<p align = center> MarkMonitor Whois Search </p>

And I found the same phone number on both websites.

<p align = center> 
  
  <img src="https://user-images.githubusercontent.com/84057292/134809542-994be3cd-3565-448e-af05-61dbc799facd.png" alt = "Who.is">

  <img src="https://user-images.githubusercontent.com/84057292/134809581-a974fb6e-2c5d-403b-9205-4b1ae3a27e24.png" alt = "MarkMonitor Whois Search">
  
</p>

So, I got the flag is the phone number.

## FLAG

`DUCTF{+61.420091337}`

# CHALLENGE NAME: Get over it!

## DESCRIPTION

Bridget loves bridges, this one is her favourite.

What is the name of it and the length of its main span to the nearest metre?

Flag format: DUCTF{the_bridge_name-#m}

## ATTACHMENT

[get-over-it.jpg](https://play.duc.tf/files/f0fe8c066ef0e50d3e409163452dabe6/get-over-it.jpg?token=eyJ1c2VyX2lkIjoyNDM3LCJ0ZWFtX2lkIjoxNDA4LCJmaWxlX2lkIjo2OX0.YVBz1w.AqPLFn4k_eN96XynWHynXrcGPdw)

## SOLUTION

I used [Yandex.com](https://yandex.com/) to search for things related to the photo. And I found this [site](https://visaknowledge.wordpress.com/australia/) talk about **5 Best Student Cities in Australia in 2018 Where to study**. I discovered in the Brisbane section there is a picture that looks quite similar to the bridge in our picture. So I searched with the keyword `bridge in brisbane`. And I saw the suggestion of Google.

![image](https://user-images.githubusercontent.com/84057292/134810560-3aba6967-dc54-4870-aa36-95f481a21109.png)

Here I see the 2nd bridge is very similar to our previous 2. So I think this is the one I need. I search on Google and found some result of main span like 183m, 184m, 185m. So I determined try with this result and finally I got the right flag with 183m of main span.

## FLAG

`DUCTF{Eleanor_Schonell-183m)`

