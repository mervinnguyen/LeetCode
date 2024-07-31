#The set [1,2,3, ..., n] contrains a total of n! unique permutations.

#By listing and labeling all of the permutations in order, we get the following sequence for n=3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"

#Given n and k, return the kth permutation sequence.

#Example 1:
#Input: n = 3, k = 3
#Output: "213"

#Example 2:
#Input: n = 4, k = 9
#Output: "2314"

#Example 3:
#Input: n = 3, k = 1
#Output: "123"

class Solution(object):
    def getPermutation(self, x, k):
        def factorial(x):
            if x == 0:
                return 1
            return x * factorial(x-1)
        nums = [str(i) for i in range(1,n+1)]
        k -= 1
        res = []
        for i in range(x,0,-1):
            index = k // factorial(i-1)
            k = k % factorial(i-1)
            res.append(nums.pop(index))
        return "".join(res)