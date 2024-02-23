"""Count the number of elements in a list
Input: nums = [2,2,1,1,1,2,3,5,5]
o/p:{2: 3, 1: 3, 3: 1, 5: 2}
"""
def number_occurences(nums):
    num_dict={}
    for num in nums:
        if num in num_dict:
            num_dict[num]+=1
        else:
            num_dict[num]=1
    return num_dict
nums = [2,2,1,1,1,2,3,5,5]
number_occurences(nums)    
