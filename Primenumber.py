import random as r
prime=[]
y=[]
for i in range(0,150):
    x=r.randint(0,1000)
    if(x==2):
        prime.append(x)
    elif(x>1):
        for j in range(2,int(x/2)):
            flag=0
            if x%j==0:
                flag=1
                break
            else:
                flag=0
        if flag==0:
            prime.append(x)
    y.append(x)
print("Prime numbers:",prime)  
z=[*set(prime)]
print(z)
