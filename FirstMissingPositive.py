#Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums. 
#You must implement an algorithm that runs in O(n) time and uses 0(1) auxiliary space.

#Example 1:
#Input: nums = [1,2,0]
#Output: 3
#Explanation: The numbers in the range [1,2] are all in the array.

#Example 2:
#Input: nums = [3,4,-1,1]
#Output: 2
#Explanation: 1 is in the array but 2 is missing.

#Example 3:
#Input: nums = [7,8,9,11,12]
#Output: 1
#Explanation: The smallest positive integer 1 is missing. 

class solution(object):
    def firstMissingPositive(self, nums):
        x = len(nums)
        for i in range(x):
            while 1 <= nums[i] <= x and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(x):
            if nums[i] != i + 1:
                return i + 1
        return x + 1