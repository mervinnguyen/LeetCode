#Given an m x n matrix, return all elements of the matrix in spiral order.

#Example 1:
#Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
#Output: [1,2,3,6,9,8,7,4,5]

#Example 2:
#Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution(object):
    def spiralOrder(self, matrix):
        x = []
        while matrix:
            x += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    x.append(row.pop())
            if matrix:
                x += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    x.append(row.pop(0))
        return x