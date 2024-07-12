#Given two integers dividennd and divisor, divide two integers without using multiplication, division, and mod operator. 

#The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

#Return the quotient after dividing dividend by divisor. 

#Example 1:
#Input: dividend = 10, divisor = 3
#Output: 3
#Explanation: 10/3 = 3.33333... Truncate it to 3.

#Example 2:
#Input: dividend = 7, divisor = -3
#Output: -2
#Explanation: 7/-3 = -2.3333... Truncate it to -2.

class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == 2**31 - 1 and divisor == 1:
            return 2**31 - 1
        if dividend == 2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == -2**31 and divisor == 1:
            return -2**31
        sign = 1
        if dividend < 0:
            dividend = -dividend
            sign = -sign
        if divisor < 0:
            divisor = -divisor
            sign = -sign
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        return res * sign