"""
[Description]
Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

 
Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

 
Constraints:

  1 <= s.length <= 5 * 104
  0 <= k <= 50

[Metadata]
- Difficulty: Medium
- Topics: Hash Table, String, Sliding Window
- Slug: longest-substring-with-at-most-k-distinct-characters
"""

// [Solution]
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        freq = {}
        max_len = 0
        for right in range(len(s)):
            ch = s[right]
            freq[ch] = freq.get(ch,0) + 1

            while len(freq) > k:
                left_ch = s[left]
                freq[left_ch] -= 1

                if freq[left_ch] == 0:
                    del freq[left_ch]

                left += 1
            max_len = max(right-left+1, max_len)
        return max_len