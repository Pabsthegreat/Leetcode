"""
[Description]
Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 
Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

 
Constraints:

  1 <= s.length <= 1000
  s consists of lowercase English letters.

[Metadata]
- Difficulty: Medium
- Topics: Two Pointers, String, Dynamic Programming
- Slug: palindromic-substrings
"""

// [Solution]
class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        t = "^#"+"#".join(s)+"#$"
        right = 0
        center = 0
        p = [0]*len(t)
        for i in range(1,len(t)-1):
            mirror = 2*center-i
            
            if i < right:
                p[i] = min(p[mirror], right - i)
            
            while t[i+p[i]+1] == t[i-p[i]-1]:
                p[i] += 1
            
            if i+p[i] > right:
                right = p[i] + i
                center = i
        return sum(((p[i]+1)//2) for i in range(len(t)))