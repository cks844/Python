#Find the product of fibonnaci series from A to B
def product(A,B):
    num1=0
    num2=1
    new_list=[0,1]
    res=0
    prod=1
    for i in range(2,B+1):
        res=num1+num2
        new_list.append(res)
        num1=num2
        num2=res
    print(new_list)
    for i in new_list[A:B+1]:
        prod=prod*i
    return prod
prod=product(2,5)
