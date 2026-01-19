"""
[Description]
Reverse Integer
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 
Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

 
Constraints:

  -231 <= x <= 231 - 1

[Metadata]
- Difficulty: Medium
- Topics: Math
- Slug: reverse-integer
"""

// [Solution]
class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        INT_MAX = 2**31 - 1  # 2147483647

        while x:
            pop = x % 10
            x //= 10
            # If rev will exceed INT_MAX after *10 + pop, return 0
            if rev > (INT_MAX - pop) // 10:
                return 0

            rev = rev * 10 + pop

        return sign * rev