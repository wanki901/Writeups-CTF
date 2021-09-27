# CHALLENGE NAME: no strings

## DESCRIPTION

This binary contains a free flag. No strings attached, seriously!

## ATTACHMENT'

[nostrigns](https://play.duc.tf/files/0b78da27e56eb98265e97fceb0ee7e3d/nostrings?token=eyJ1c2VyX2lkIjoyNDM3LCJ0ZWFtX2lkIjoxNDA4LCJmaWxlX2lkIjo3N30.YVH7Jw.jRiMceELMJW9rEppVnZ2oeVPpVs)

## SOLUTION

Use IDA Pro to decompiled the file. In main function, I saw a variable named `format` that has a tag `flag?`.
<p align = center>
  <img src="https://user-images.githubusercontent.com/84057292/134955540-a71d265a-0a3c-427a-9b3d-f03d9761d4dd.png">
</p>

So, I double click it to check it. And I saw the flag near by it.

<p align = center>
  <img src="https://user-images.githubusercontent.com/84057292/134955722-f0795f19-be88-4665-ba48-8527dd18b236.png>
</p>
## FLAG

`DUCTF{stringent_strings_string}`
