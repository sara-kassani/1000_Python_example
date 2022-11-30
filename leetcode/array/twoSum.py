# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
class Solution:
	def twoSum(self, nums, target):
		dic={}
		for i in range(len(nums)):
			if (target-nums[i]) not in dic:
				dic[nums[i]]=i
			else:
				return [dic[target-nums[i]],i]


class Solution1:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
 

if __name__=='__main__':
    solution= Solution()
    lst= [1, 2, 3, 4, 5]
    target=5
    result= solution.twoSum(lst, target)
    print(result)      # [1, 2]
