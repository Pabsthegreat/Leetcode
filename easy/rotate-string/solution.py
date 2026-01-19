"""
[Description]
Rotate String
https://leetcode.com/problems/rotate-string/

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

A shift on s consists of moving the leftmost character of s to the rightmost position.

  For example, if s = "abcde", then it will be "bcdea" after one shift.

 
Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true
Example 2:
Input: s = "abcde", goal = "abced"
Output: false

 
Constraints:

  1 <= s.length, goal.length <= 100
  s and goal consist of lowercase English letters.

[Metadata]
- Difficulty: Easy
- Topics: String, String Matching
- Slug: rotate-string
"""

// [Solution]
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        shift = len(s)
        while shift>0 and s != goal:
            s = s[1:]+s[0]
            shift-=1
        if shift>0:
            return True

        return False
