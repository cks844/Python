#Write a program to add the sum of digits in two lists and print the reverse of the sum
#l1=[2,4,3]
#l2=[5,6,4]
#o/p is 708(reverse of 807)
def addTwoNumbers(l1, l2):
    num1 = int(''.join(map(str, l1[::-1]))) #convert the list to integers
    num2 = int(''.join(map(str, l2[::-1])))
    s=str(num1+num2)
    v=""
    for i in s:
        v=i+v
    print(v)
l1 = [2,4,3]
l2 = [5,6,4]
add=addTwoNumbers(l1,l2)
