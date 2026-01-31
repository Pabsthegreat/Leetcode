"""
[Description]
Sudoku Solver
https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

  Each of the digits 1-9 must occur exactly once in each row.
  Each of the digits 1-9 must occur exactly once in each column.
  Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.

 
Example 1:

Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:

 
Constraints:

  board.length == 9
  board[i].length == 9
  board[i][j] is a digit or '.'.
  It is guaranteed that the input board has only one solution.

[Metadata]
- Difficulty: Hard
- Topics: Array, Hash Table, Backtracking, Matrix
- Slug: sudoku-solver
"""

// [Solution]
class Solution(object):
    def solveSudoku(self, board):
        boxes = {i:set() for i in range(9)}
        rows = {i:set() for i in range(9)}
        columns = {i:set() for i in range(9)}
        vals = {str(i) for i in range(1,10)}
        
        def populate(board):
            for row in range(9):
                for column in range(9):
                    val = board[row][column]
                    if val != ".":
                        box = (row//3)*3 + column//3
                        boxes[box].add(val)
                        rows[row].add(val)
                        columns[column].add(val)

        def solve(board, start_row, start_column):
            for row in range(start_row, 9):
                # Only use start_column for the starting row
                col_start = start_column if row == start_row else 0
                for column in range(col_start, 9):
                    if board[row][column] == ".":
                        box = (row//3)*3 + column//3
                        p_vals = vals - rows[row] - columns[column] - boxes[box]
                        if not p_vals:
                            return False
                        
                        for val in p_vals:
                            board[row][column] = val
                            rows[row].add(val) 
                            columns[column].add(val) 
                            boxes[box].add(val)
                            
                            # Calculate next position
                            next_col = column + 1
                            if next_col == 9:
                                next_row = row + 1
                                next_col = 0
                            else:
                                next_row = row
                            
                            if solve(board, next_row, next_col):
                                return True
                            
                            # Backtrack
                            board[row][column] = "."
                            rows[row].remove(val) 
                            columns[column].remove(val) 
                            boxes[box].remove(val)
                        
                        return False  # No valid value found
            return True  # All cells filled

        populate(board)
        solve(board, 0, 0)