l=[1,2,3,3,5,5,7]
for i in l:
    counter=0
    for j in l:
        if i==j:
            counter+=1
    if counter > 1:
        print(i,end=" ")
print('\n')
for i in range(len(l)-1):
    if l[i+1]-l[i]!=1 and l[i+1]-l[i]==0 :
        print(l[i]+1)    
