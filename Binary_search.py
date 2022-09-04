def binary_search(l):
    x=int(input("Number to search:"))
    c=0
    first=0
    last=len(l)-1
    while(first<=last):
        c+=1
        mid=(first+last)//2
        if(x==l[mid]):
            print(str(x)+" ""is in the list")
            print("No of iterations:",c)
            break
        elif(x<l[mid]):
            last=mid-1
        else:
            first=mid+1
        
    if(first>last):
        print(str(x)+" ""is not in the list")
l=[1,2,3,4,5,6,7,8,9,10]
binary_search(l)    
