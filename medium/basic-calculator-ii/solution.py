"""
[Description]
Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/

Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 
Example 1:
Input: s = "3+2*2"
Output: 7
Example 2:
Input: s = " 3/2 "
Output: 1
Example 3:
Input: s = " 3+5 / 2 "
Output: 5

 
Constraints:

  1 <= s.length <= 3 * 105
  s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
  s represents a valid expression.
  All the integers in the expression are non-negative integers in the range [0, 231 - 1].
  The answer is guaranteed to fit in a 32-bit integer.

[Metadata]
- Difficulty: Medium
- Topics: Math, String, Stack
- Slug: basic-calculator-ii
"""

// [Solution]
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        op = '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                number = number * 10 + int(ch)

            if ch in '+-*/' or i == len(s) - 1: #process using previous operator
                if op == '+':
                    stack.append(number)

                elif op == '-':
                    stack.append(-number)

                elif op == '*':
                    stack.append(stack.pop() * number)

                elif op == '/':
                    prev = stack.pop()
                    stack.append(int(prev / number))  # truncate toward 0

                op = ch #assign currently seen operator
                number = 0

        return sum(stack)