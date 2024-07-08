#Given an integer array nums and an integer val, remove all occurences of val in nums in-place. The order of the elements may be changed.
#Then return the number of eleements in nums which are not equal to val.

#Consider the number of elements in nums which are not equal to val to be k, to get accepeted, you need to do the following things:

#Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
#The remaining elements of nums are not important as wlel as the size of nums.
#Return K.

#Example 1:
#Input: nums = [3,2,2,3], val = 3
#Output: 2, nums = [2,2,_,_]

#Example 2:
#Input: nums = [0,1,2,2,3,0,4,2], val = 2
#Output: 5, nums = [0,1,4,0,3,_,_,_]

class Solution(object):
    def removeElement(self, nums, val):
        m = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                 m = m + 1
        return m