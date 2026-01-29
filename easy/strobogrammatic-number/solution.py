"""
[Description]
Strobogrammatic Number
https://leetcode.com/problems/strobogrammatic-number/

Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

 
Example 1:

Input: num = "69"
Output: true

Example 2:

Input: num = "88"
Output: true

Example 3:

Input: num = "962"
Output: false

 
Constraints:

  1 <= num.length <= 50
  num consists of only digits.
  num does not contain any leading zeros except for zero itself.

[Metadata]
- Difficulty: Easy
- Topics: Hash Table, Two Pointers, String
- Slug: strobogrammatic-number
"""

// [Solution]
class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        d = {"6":"9","9":"6","1":"1","8":"8","0":"0"}
        s = ""
        for i in num:
            if i in d:
                s=d[i]+s
            else:
                return False
        return s==num