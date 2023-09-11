"""Count the number of elements in a list
Input: nums = [2,2,1,1,1,2,2,3]
o/p:[1,3,4]
"""
nums = [2,2,1,1,1,2,2,3]
new=[]
for i in nums:
    new.append(nums.count(i))
new[:]=set(new)
new
