"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""
nums = [0,0,1,1,1,2,2,3,3,4]
duplicates=0

for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        duplicates += 1
    else:
        nums[i - duplicates] = nums[i]
    
    print("i: {}, nums[i]: {}, nums[i-1]: {}, duplicates: {}, nums[i-duplicates]: {}".format(i, nums[i], nums[i-1], duplicates, nums[i-duplicates]))
    print("duplicates: ", duplicates)
    
    print("len(nums) - duplicates: ", len(nums) - duplicates)
    
i: 1, nums[i]: 0, nums[i-1]: 0, duplicates: 1, nums[i-duplicates]: 0
duplicates:  1 ===== len(nums) - duplicates:  9
i: 2, nums[i]: 1, nums[i-1]: 1, duplicates: 1, nums[i-duplicates]: 1
duplicates:  1 ===== len(nums) - duplicates:  9
i: 3, nums[i]: 1, nums[i-1]: 1, duplicates: 2, nums[i-duplicates]: 1
duplicates:  2 ===== len(nums) - duplicates:  8
i: 4, nums[i]: 1, nums[i-1]: 1, duplicates: 3, nums[i-duplicates]: 1
duplicates:  3 ===== len(nums) - duplicates:  7
i: 5, nums[i]: 2, nums[i-1]: 1, duplicates: 3, nums[i-duplicates]: 2
duplicates:  3 ===== len(nums) - duplicates:  7
i: 6, nums[i]: 2, nums[i-1]: 2, duplicates: 4, nums[i-duplicates]: 2
duplicates:  4 ===== len(nums) - duplicates:  6
i: 7, nums[i]: 3, nums[i-1]: 2, duplicates: 4, nums[i-duplicates]: 3
duplicates:  4 ===== len(nums) - duplicates:  6
i: 8, nums[i]: 3, nums[i-1]: 3, duplicates: 5, nums[i-duplicates]: 3
duplicates:  5 ===== len(nums) - duplicates:  5
i: 9, nums[i]: 4, nums[i-1]: 3, duplicates: 5, nums[i-duplicates]: 4
duplicates:  5 ===== len(nums) - duplicates:  5
