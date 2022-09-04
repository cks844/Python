def linear_search(n):
    element=list(range(1,n))
    count=0
    flag=0
    x=int(input("Number to be searched:"))
    for i in element:
        count+=1
        if(i==x):
            print(str(x)+" ""is in the list")
            flag=1
            break
    if(flag==0):
        print(str(x)+" ""not found in the list")
    print("No of iterations:"+str(count))
linear_search(50)
