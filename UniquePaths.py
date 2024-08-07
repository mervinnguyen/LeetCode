#There is a robot on an m x n grid. The robot is initially located at the top-left corner (0, 0). The robot is initally located at the top-left corner. The robot tries to move to the bottom-right corner. The robot can move either down or right at any point in time.

#Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner. 

#The test cases are generated so that the answer will be less than or equal to 2 * 10^9

class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]