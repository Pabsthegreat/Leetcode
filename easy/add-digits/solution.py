"""
[Description]
Add Digits
https://leetcode.com/problems/add-digits/

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 
Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0

 
Constraints:

  0 <= num <= 231 - 1

 
Follow up: Could you do it without any loop/recursion in O(1) runtime?

[Metadata]
- Difficulty: Easy
- Topics: Math, Simulation, Number Theory
- Slug: add-digits
"""

// [Solution]
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def add(n):
            if 10 > n:
                return n
            q = n//10
            r = n%10
            return add(q+r)
        return add(num)