l=[1,1,1,2,2,3,4,5,5,6]
x=1
for i in l:
    flag=0
    for j in l:
        if i==j:
            flag+=1
        if flag>=1:
            if i in l:
                l.remove(i)
print(l)
