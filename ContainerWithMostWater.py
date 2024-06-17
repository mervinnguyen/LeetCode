#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, height[i]) and (i, 0). 

#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#Return the maximum amount of water that can be held.

#Example 1:
#Input: height = [1,8,6,2,5,4,8,3,7]
#Output: 49
#Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

#Example 2:
#Input: height = [1,1]
#Output: 1

class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area