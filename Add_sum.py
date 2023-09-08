#Write a program to add the sum of digits in two lists and print the reverse of the sum
#l1=[2,4,3]
#l2=[5,6,4]
#o/p is 708(reverse of 807)
def addTwoNumbers(l1, l2):
    num1 = int(''.join(map(str, l1[::-1]))) #convert the list to integers
    num2 = int(''.join(map(str, l2[::-1])))
    res=str(num1+num2)
    print(res[::-1])
l1 = [2,4,3]
l2 = [5,6,4]
add=addTwoNumbers(l1,l2)

#Solution-2(for printing the sum as a list)Eg:[7,0,8]
def addTwoNumbers(l1, l2):
    num1 = int(''.join(map(str, l1[::-1]))) #convert the list to integers
    num2 = int(''.join(map(str, l2[::-1])))
    s=str(num1+num2)
    res_list= [int(digit) for digit in res_list][::-1] 
    print(res_list)
l1 = [2,4,3]
l2 = [5,6,4]
add=addTwoNumbers(l1,l2)
