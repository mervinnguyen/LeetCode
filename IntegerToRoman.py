#Seven different symbols represent Roman numerals with the following values:
#I = 1
#V = 5
#X = 10
#L = 50
#C = 100
#D = 500
#M = 1000

#Roman numerals are formed by appending the conversion of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

#If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append the symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
#If the value starts with 4 or 9, use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1(I) less than 10(X): IX. Only the following
#subtractions are allowed: IV (4), IX (9), XL (40), XC (90), CD (400), CM (900).

#Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5(V), 50(L), or 500(D) multiple times. If you need to append a symbol 4 times use the subtractive form. 

#Given an integer, conver it to a Roman numeral.

#Example 1:
#Input: num = 3749
#Output: "MMMDCCXLIX"

class Solution(object):
    def intToRoman(self,num):
        roman = ''
        while num > 0:
            if num >= 1000:
                roman += 'M'
                num -= 1000
            elif num >= 900:
                roman += 'CM'
                num -= 900
            elif num >= 500:
                roman += 'D'
                num -= 500
            elif num >= 400:
                roman += 'CD'
                num -= 400
            elif num >= 100:
                roman += 'C'
                num -= 100
            elif num >= 90:
                roman += 'XC'
                num -= 90
            elif num >= 50:
                roman += 'L'
                num -= 50
            elif num >= 40:
                roman += 'XL'
                num -= 40
            elif num >= 10:
                roman += 'X'
                num -= 10
            elif num >= 9:
                roman += 'IX'
                num -= 9
            elif num >= 5:
                roman += 'V'
                num -= 5
            elif num >= 4:
                roman += 'IV'
                num -= 4
            elif num >= 1:
                roman += 'I'
                num -= 1
        return roman