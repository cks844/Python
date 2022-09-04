def linear_search():
    element=[]
    for i in range(1,101):
        element.append(i)
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
linear_search()
