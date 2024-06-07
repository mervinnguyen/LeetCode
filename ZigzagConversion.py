#Zig Zag Conversion 

#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

#P   A   H   N
#A P L S I I G
#Y   I   R

#And then read line by line: "PAHNAPLSIIGY"
#Write the code that will take a string and make this conversion given a number of rows.
#string convert(string s, int numRows);

#Example 1:
#Input: s = "PAYPALISHIRING", numRows = 3
#Output: "PAHNAPLSIIGY"

#Example 2:
#Input: s = "PAYPALISHIRING", numRows = 4
#Output: "PINALSIGYAHRPI"
#Explanation:
#P     I    N
#A   L S  I G
#Y A   H R
#P     I

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        n = len(s)
        cycle = 2 * numRows - 2
        result = []
        for i in range(numRows):
            for j in range(i, n, cycle):
                result.append(s[j])
                if i != 0 and i != numRows - 1 and j + cycle - 2 * i < n:
                    result.append(s[j + cycle - 2 * i])
        return "".join(result)
