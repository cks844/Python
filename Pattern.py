#Write a program to take an integer N as an input and display the pattern#

N=int(input())
for i in range(N):
    for j in range(i+1):
         print('* ',end="")
    print()
for i in range(N-1,0,-1):
    for j in range(i):
        print("* ",end="")
    if j!=0:
        print()
