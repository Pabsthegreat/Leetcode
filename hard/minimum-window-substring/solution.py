"""
[Description]
Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 
Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

 
Constraints:

  m == s.length
  n == t.length
  1 <= m, n <= 105
  s and t consist of uppercase and lowercase English letters.

 
Follow up: Could you find an algorithm that runs in O(m + n) time?

[Metadata]
- Difficulty: Hard
- Topics: Hash Table, String, Sliding Window
- Slug: minimum-window-substring
"""

// [Solution]
from collections import Counter, defaultdict
from typing import List

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        window = defaultdict(int)

        required = len(need)   # number of unique chars needed
        formed = 0             # number of unique chars currently satisfied

        l = 0
        best_len = float("inf")
        best_l = 0
        best_r = 0

        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            if char in need and window[char] == need[char]:
                formed += 1

            while formed == required:
                curr_len = r - l + 1

                if curr_len < best_len:
                    best_len = curr_len
                    best_l = l
                    best_r = r

                left_char = s[l]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                l += 1

        if best_len == float("inf"):
            return ""

        return s[best_l:best_r + 1]