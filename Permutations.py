#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

#Example 1:
#Input: nums = [1,2,3]
#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

#Example 2:
#Input: nums = [0,1]
#Output: [[0,1],[1,0]]

#Example 3:
#Input: nums = [1]
#Output: [[1]]

class Solution(object):
    def permute(self, nums):
        def backtrack(num1 = 0):
            if num1 == a:
                output.append(nums[:])
            for i in range(num1, a):
                nums[num1], nums[i] = nums[i], nums[num1]
                backtrack(num1 + 1)
                nums[num1], nums[i] = nums[i], nums[num1]
        a = len(nums)
        output = []
        backtrack()
        return output