#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also reporesented as a string.

#Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Example 1:
#Input: num1 = "2", num2 = "3"
#Output: "6"

#Example 2:
#Input: num1 = "123", num2 = "456"
#Output: "56088"

class Solution(object):
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        x, y = len(num1), len(num2)
        result = [0] * (x + y)
        for i in range(x - 1, -1, -1):
            for j in range(y - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                summ = mul + result[p2]
                result[p1] += summ // 10
                result[p2] = summ % 10
        return ''.join(map(str, result)).lstrip('0')