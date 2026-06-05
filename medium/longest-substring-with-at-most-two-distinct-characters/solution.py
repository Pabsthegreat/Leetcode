"""
[Description]
Longest Substring with At Most Two Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/

Given a string s, return the length of the longest substring that contains at most two distinct characters.

 
Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

 
Constraints:

  1 <= s.length <= 105
  s consists of English letters.

[Metadata]
- Difficulty: Medium
- Topics: Hash Table, String, Sliding Window
- Slug: longest-substring-with-at-most-two-distinct-characters
"""

// [Solution]
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        freq = {}
        max_len = 0

        for right in range(len(s)):
            ch = s[right]
            freq[ch] = freq.get(ch, 0) + 1

            while len(freq) > 2:
                left_ch = s[left]
                freq[left_ch] -= 1

                if freq[left_ch] == 0:
                    del freq[left_ch]

                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
