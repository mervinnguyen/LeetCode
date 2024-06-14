#Given a string s and pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

#Example 1:
#Input: s = "aa", p = "a"
#Output: false
#Explanation: "a" does not match the entire string "aa".

#Example 2:
#Input: s = "aa", p = "a*"
#Output: true
#Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

#Example 3:
#Input: s = "ab", p = ".*"
#Output: true
#Explanation: ".*" means "zero or more (*) of any character (.)".

class Solution(object):
    def isMatch(self,s,p):
        if not p:
            return not s
        firstMatch = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s,p[2:]) or firstMatch and self.isMatch(s[1:],p))
        else:
            return firstMatch and self.isMatch(s[1:],p[1:])

