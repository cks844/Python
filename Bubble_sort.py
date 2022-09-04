def bubblesort(a):
    n=len(a)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
print("The sorted array",a)   
a=[5,4,9,3,1]
bubblesort(a)
