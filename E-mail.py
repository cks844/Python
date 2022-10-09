import re
def mail1_check():
    id=input("Enter e-mail id to verify:")
    check="^[a-zA-Z0-9-_]+@[a-zA-Z]+\.['com']{1,3}$"
    if re.match(check,id):
        print("Your mail-id is valid")
    else:
        print("Not valid")
def mail2_check():
    id=input("Enter e-mail id to verify:")
    check="^[a-zA-Z0-9-_]+@[a-zA-Z.]+\.[a-z]+\.['in']{1,3}$"
    if re.match(check,id):
        print("Your college mail-id is valid")
    else:
        print("Invalid college mail-id")
def mail3_check():
    id=input("Enter e-mail id to verify:")
    check="^[a-zA-Z0-9-_]+@[a-zA-Z.]+\.['org']{1,3}$"
    if re.match(check,id):
        print("Your mail-id is valid")
    else:
        print("Invalid")
def check():
    while(True):
        print("G-mail:0\nCollege-id=1\nOrg=2")
        inp=int(input())
        if inp==0:
            mail1_check()
        elif inp==1:
            mail2_check()
        elif inp==2:
            mail3_check()
        else:
            print("Invalid input")
            check()
    return True
    
check()
