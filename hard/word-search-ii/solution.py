"""
[Description]
Word Search II
https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 
Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

 
Constraints:

  m == board.length
  n == board[i].length
  1 <= m, n <= 12
  board[i][j] is a lowercase English letter.
  1 <= words.length <= 3 * 104
  1 <= words[i].length <= 10
  words[i] consists of lowercase English letters.
  All the strings of words are unique.

[Metadata]
- Difficulty: Hard
- Topics: Array, String, Backtracking, Trie, Matrix
- Slug: word-search-ii
"""

// [Solution]
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # Build trie
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        rows = len(board)
        cols = len(board[0])
        res = []

        def dfs(r, c, node):
            # out of bounds
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            ch = board[r][c]

            # already used in this path
            if ch == "#":
                return

            # current path is not a prefix of any word
            if ch not in node.children:
                return

            next_node = node.children[ch]

            # found complete word
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None  # avoid duplicate answers

            # mark visited
            board[r][c] = "#"

            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            # backtrack
            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res