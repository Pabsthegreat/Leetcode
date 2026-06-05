"""
[Description]
Generate Parentheses
https://leetcode.com/problems/generate-parentheses/

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]

 
Constraints:

  1 <= n <= 8

[Metadata]
- Difficulty: Medium
- Topics: String, Dynamic Programming, Backtracking
- Slug: generate-parentheses
"""

// [Solution]
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        arr = []

        def generate(st, open, close):
            if open == 0 and close == 0:
                arr.append(st)
                return

            if open > 0:
                generate(st + "(", open - 1, close)

            if close > open:
                generate(st + ")", open, close - 1)

        generate("", n, n)
        return arr