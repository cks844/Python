#Python program to find the product of elements in a list except an element
# Input : [1,2,3,4,5] 
# Output : [24,12,8,6]
def prod(l):
    prod = 1
    for i in l:
        prod *= i
    new_list=[]
    for j in range(len(l)):
        new_list.append(int(prod/l[j]))
    return (new_list)
l = [1,2,3,4,5]
prod(l)
