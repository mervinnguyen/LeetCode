#Given a pair of parantheses, write a function to generate all combinations of well-formed parentheses.

#Example 1:
#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]

#Example 2:
#Input: n = 1
#Output: ["()"]

#Constraints:
#1 <= n <= 8

class Solution(object):
    def generateParenthesis(self, n):
        def back(s = '', left = 0, right = 0):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                back(s + '(', left + 1, right)
            if right < left:
                back(s + ')', left, right + 1)
        
        result = []
        back()
        return result