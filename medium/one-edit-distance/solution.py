"""
[Description]
One Edit Distance
https://leetcode.com/problems/one-edit-distance/

Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

  Insert exactly one character into s to get t.
  Delete exactly one character from s to get t.
  Replace exactly one character of s with a different character to get t.

 
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.

Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.

 
Constraints:

  0 <= s.length, t.length <= 104
  s and t consist of lowercase letters, uppercase letters, and digits.

[Metadata]
- Difficulty: Medium
- Topics: Two Pointers, String
- Slug: one-edit-distance
"""

// [Solution]
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
        l1 = len(s)
        l2 = len(t)
        dif = l1-l2
        if abs(dif) > 1:
            return False
        if l1 + l2 == 1:
            return True

        if dif == 0:
            flag = 0
            for i in range(l1):
                if s[i] != t[i]:
                    if flag == 1:
                        return False
                    flag += 1
            if flag == 1:
                return True

        elif dif == 1:
            flag = 0
            i,j = 0,0
            while i < l1 and j < l2:
                if s[i] != t[j]:
                    if flag == 1:
                        return False
                    flag += 1
                    i+=1
                else:
                    i += 1
                    j += 1
            if flag == 1 or i == l1 - 1:
                return True
        
        elif dif == -1:
            flag = 0
            i,j = 0,0
            while i < l1 and j < l2:
                if s[i] != t[j]:
                    if flag == 1:
                        return False
                    flag += 1
                    j+=1
                else:
                    i += 1
                    j += 1
            if flag == 1 or j == l2 - 1:
                return True
        return False