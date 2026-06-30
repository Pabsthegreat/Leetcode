"""
[Description]
Surrounded Regions
https://leetcode.com/problems/surrounded-regions/

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

  Connect: A cell is connected to adjacent cells horizontally or vertically.
  Region: To form a region connect every 'O' cell.
  Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.

To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

 
Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

Explanation:

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:

Input: board = [["X"]]

Output: [["X"]]

 
Constraints:

  m == board.length
  n == board[i].length
  1 <= m, n <= 200
  board[i][j] is 'X' or 'O'.

[Metadata]
- Difficulty: Medium
- Topics: Array, Depth-First Search, Breadth-First Search, Union-Find, Matrix
- Slug: surrounded-regions
"""

// [Solution]
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])

        def dfs(r, c):
            if (
                r < 0 or r >= row or
                c < 0 or c >= col or
                board[r][c] != "O"
            ):
                return

            board[r][c] = "S"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Mark border-connected O's as safe
        for r in range(row):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][col - 1] == "O":
                dfs(r, col - 1)

        for c in range(col):
            if board[0][c] == "O":
                dfs(0, c)
            if board[row - 1][c] == "O":
                dfs(row - 1, c)

        # 2. Flip surrounded O's to X, and safe S back to O
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"