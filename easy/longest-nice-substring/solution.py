"""
[Description]
Longest Nice Substring
https://leetcode.com/problems/longest-nice-substring/

A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 
Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.

 
Constraints:

  1 <= s.length <= 100
  s consists of uppercase and lowercase English letters.

[Metadata]
- Difficulty: Easy
- Topics: Hash Table, String, Divide and Conquer, Bit Manipulation, Sliding Window
- Slug: longest-nice-substring
"""

// [Solution]
class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return ""
        d = ord("a") - ord("A")
        r = ""
        w = list(s)
        for i in s:
            m = ""
            for j in w:
                m+=j
                if len(m) > 1:
                    f = True
                    s1 = list(m)
                    for k in s1:
                        if k.swapcase() not in s1:
                            f = False
                            break

                    if f == True and len(m) > len(r):
                        r = m
            w.pop(0)
        return r


                
                