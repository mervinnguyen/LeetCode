#Determine if a 9x9 Sudoku board is valid. Only the filled cells needs to be validated according to the rules:
#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

#Example 1: 
#Input: board =
#[["5","3",".",".","7",".",".",".","."],
#["6",".",".","1","9","5",".",".","."],
#[".","9","8",".",".",".",".","6","."],
#["8",".",".",".","6",".",".",".","3"],
#["4",".",".","8",".","3",".",".","1"],
#["7",".",".",".","2",".",".",".","6"],
#[".","6",".",".",".",".","2","8","."],
#[".",".",".","4","1","9",".",".","5"],
#[".",".",".",".","8",".",".","7","9"]]

#Output: true

#Example 2:
#Input: board =
#[["8","3",".",".","7",".",".",".","."],
#["6",".",".","1","9","5",".",".","."],
#[".","9","8",".",".",".",".","6","."],
#["8",".",".",".","6",".",".",".","3"],
#["4",".",".","8",".","3",".",".","1"], 
#["7",".",".",".","2",".",".",".","6"],
#[".","6",".",".",".",".","2","8","."],
#[".",".",".","4","1","9",".",".","5"],
#[".",".",".",".","8",".",".","7","9"]]
#Output: false

class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
                if board[i][j] in boxes[(i // 3) * 3 + j // 3]:
                    return False
                boxes[(i // 3) * 3 + j // 3].add(board[i][j])
        return True
