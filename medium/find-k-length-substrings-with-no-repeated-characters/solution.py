"""
[Description]
Find K-Length Substrings With No Repeated Characters
https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

 
Example 1:

Input: s = "havefunonleetcode", k = 5
Output: 6
Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.

Example 2:

Input: s = "home", k = 5
Output: 0
Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.

 
Constraints:

  1 <= s.length <= 104
  s consists of lowercase English letters.
  1 <= k <= 104

[Metadata]
- Difficulty: Medium
- Topics: Hash Table, String, Sliding Window
- Slug: find-k-length-substrings-with-no-repeated-characters
"""

// [Solution]
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        nos = 0
        left = 0
        freq = {}

        for right in range(len(s)):
            ch = s[right]
            freq[ch] = freq.get(ch,0) + 1

            if right + 1 > k:
                left_ch = s[left]
                freq[left_ch] -= 1
                if freq[left_ch] == 0:
                    del freq[left_ch]
                left += 1

            if len(freq) == k:
                nos += 1
        return nos