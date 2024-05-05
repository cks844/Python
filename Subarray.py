#There is an array and an integer as input. 
#Divide the elements into subarray where each element in subarray contains elements with size as that of given integer. 
#Return the subarray with maximum sum value

def divide_into_subarray(arr,key):
    sub_array = []
    for i in range(0,len(arr),key):
        sub_array.append(arr[i:i+size])
    sum_array = []
    for i in sub_array:
        sum_array.append(sum(i))
    print(sub_array)
    return sub_array[sum_array.index(max(sum_array))]  
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
key = 3 
result = divide_into_subarray(arr, key)
print(result)
