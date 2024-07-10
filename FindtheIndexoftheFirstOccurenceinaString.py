#Given two strings needle and haystack, return the index of the first occurence of needle in haystack, or -1 if needle is not part of haystack.

#Example 1:
#Input: haystack = "sadbutsad", needle = "sad"
#Explanation: "sad" occurs at index 0 and 6. The first occurence is at index 0, so we return 0.

#Example 2:
#Input: haystack = "leetcode", needle = "leeto"
#Output: -1
#Explanation: "leeto" is not part of "leetcode", so we return -1.

class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1