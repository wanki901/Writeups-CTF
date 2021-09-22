# Challenge Name: MILKSLAP

## DESCRIPTION 

  An icon. When we click it, we will go to this site http://mercury.picoctf.net:48319/

  And we'll see a gif that has a man who was splashed milk by another one.

## METHODOLOGY

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

## Flag

`picoCTF{imag3_m4n1pul4t10n_sl4p5}`

# CHALLENGE NAME: DISK, DISK, SLEUTH!

## DESCRIPTION

Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: dds1-alpine.flag.img.gz

## ATTACHMENTS

[dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/920731987787c93839776ce457d5ecd6/dds1-alpine.flag.img.gz)

## METHODDOLOGY

Extract this file we have a file that has an extension `img`. An `img` file is a **disk image file** created by various disk imaging applications, such as H+H Software Virtual CD. It stores an exact copy of the data on a CD or DVD and is used for backups and burning new discs. 

`imf` files created by different disk imaging programs may use different formats. For example, IMG files created by SlySoft CloneCD must be paired with an associated `.CCD` and `.SUB` file before they can be used to create a disc. Before using an `img` file to create a new disc, you should attempt to determine what program created the `img` file and check whether your disc-authoring program can burn files saved in that format.

In Kali Linux, we have a tool which named Sleuth Kit. [Sleuth Kit](https://www.sleuthkit.org/sleuthkit/) is a collection of command line tools and a C library that allows you to analyze disk images and recover files from them. It is used behind the scenes in Autopsy and many other open source and commercial forensics tools.

So this challenge tells we forensic disk image by using `srch_string` command in Sleuth Kit.

## EXPLOIT

![image](https://user-images.githubusercontent.com/84057292/134299719-e196b085-d562-42b0-b472-5fec0ace5908.png)

## FLAG

`picoCTF{f0r3ns1c4t0r_n30phyt3_564ff1a0}`

# CHALLENGE NAME: DISK, DISK, SLEUTH II!

## DESCRIPTION

All we know is the file with the flag is named `down-at-the-bottom.txt`... Disk image: dds2-alpine.flag.img.gz

## ATTACHMENTS

[dds2-alpine.flag.img.gz](https://mercury.picoctf.net/static/2e54f22211165e9f33a47bdb8a09268b/dds2-alpine.flag.img.gz)

## METHODOLOGY

As same as previous challenge `Disk, Disk, Sleuth!`, after extrace we have a file which is a disk image file. But we don't use Sleuth Kit command in Kali Linux again, because of the decsription of this challenge let we know the name of file contains the flag. So I will use Autopsy for easy to find and check the file. [Autopsy](https://www.sleuthkit.org/autopsy/) is an easy to use, GUI-based program that allows you to efficiently analyze hard drives and smart phones. It has a plug-in architecture that allows you to find add-on modules or develop custom modules in Java or Python.

## EXPLOIT

  Open this file with Autopsy.

![image](https://user-images.githubusercontent.com/84057292/134303113-384f73fa-bcc6-4ef1-95af-79d406a140f4.png "Autopsy")

  Use `File Search by Attributes` in Tools to search nanme of the file `down-at-the-bottom.txt`
  
  ![image](https://user-images.githubusercontent.com/84057292/134305616-e8113230-2bb1-4aab-b767-16b17ead80fb.png)

I really found this file, let check it.

![image](https://user-images.githubusercontent.com/84057292/134305879-af4fc9da-8ef7-493b-9014-91c8fa88018d.png)



























