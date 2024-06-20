#Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target
#Return the sum of the three integers. 
#You may assume that each input would have exactly one solution.

#Example 1:
#Input: nums = [-1,2,1,-4], target = 1
#Output: 2
#Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

#Example 2:
#Input: nums = [0,0,0], target = 1
#Output: 0

class Solution(object):
    def threeSumClosest(self,nums,target):
        nums.sort()
        n = len(nums)
        closest = float('inf')
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(target - s) < abs(target - closest):
                    closest = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return closest