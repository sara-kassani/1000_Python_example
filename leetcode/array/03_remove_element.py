"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
"""
nums = [0,1,2,2,3,0,4,2] 
val = 2

while val in nums:
    nums.remove(val)
    print("nums", nums)
print(len(nums))

"""
nums [0, 1, 2, 3, 0, 4, 2]
nums [0, 1, 3, 0, 4, 2]
nums [0, 1, 3, 0, 4]
5
"""
