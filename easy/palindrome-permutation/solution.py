"""
[Description]
Palindrome Permutation
https://leetcode.com/problems/palindrome-permutation/

Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

 
Example 1:

Input: s = "code"
Output: false

Example 2:

Input: s = "aab"
Output: true

Example 3:

Input: s = "carerac"
Output: true

 
Constraints:

  1 <= s.length <= 5000
  s consists of only lowercase English letters.

[Metadata]
- Difficulty: Easy
- Topics: Hash Table, String, Bit Manipulation
- Slug: palindrome-permutation
"""

// [Solution]
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        flag = False
        for i in d:
            if d[i]%2 == 1:
                if not flag:
                    flag = True
                else:
                    return False
        return True
