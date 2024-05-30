#Longest Substring Without Repeating Characters

#Given a string s, find the length of the longest substring without repeating characters.

#Example 1: 
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        front = 0
        maxLength = 0
        usedChar = {}
        
        for i, char in enumerate(s):
            if char in usedChar and front <= usedChar[char]:
                front = usedChar[char] + 1
            else:
                maxLength = max(maxLength, i - front + 1)
            
            usedChar[char] = i
        
        return maxLength

s = "abcabcbb"
ret = Solution().lengthOfLongestSubstring(s)
print(ret)