def Palindrome(s):
    str = ""
    for i in s:
        str = i + str #iterates to every element and joins each character in the beginning('str+i'gives the original string)
    if(str==s):
        print("The string is a Palindrome")
    else:
        print("The string is not a Palindrome")
s =input("Enter a string")
Palindrome(s)
