#Longest Palindromic Substring

#Given a string s, return the longest palindromic substring in s.

#Example 1:
#Input: s = "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

#Example 2:
#Input: s = "cbbd"
#Output: "bb"

#Constraints 
#1 <= s.length <= 1000
#s consist of only digits and English letters (lower-case and/or upper-case)

class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        def expandAroundCenter(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        result = ""
        for i in range(n):
            odd = expandAroundCenter(i, i)
            even = expandAroundCenter(i, i+1)
            result = max(result, odd, even, key=len)
        return result