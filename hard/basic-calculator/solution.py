"""
[Description]
Basic Calculator
https://leetcode.com/problems/basic-calculator/

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 
Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

 
Constraints:

  1 <= s.length <= 3 * 105
  s consists of digits, '+', '-', '(', ')', and ' '.
  s represents a valid expression.
  '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
  '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
  There will be no two consecutive operators in the input.
  Every number and running calculation will fit in a signed 32-bit integer.

[Metadata]
- Difficulty: Hard
- Topics: Math, String, Stack, Recursion
- Slug: basic-calculator
"""

// [Solution]
class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        number = 0
        sign = 1
        stack = []

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == '+':
                result += sign * number
                number = 0
                sign = 1

            elif ch == '-':
                result += sign * number
                number = 0
                sign = -1

            elif ch == '(':
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1
                number = 0

            elif ch == ')':
                result += sign * number
                number = 0

                prev_sign = stack.pop()
                prev_result = stack.pop()

                result = prev_result + prev_sign * result

        result += sign * number
        return result