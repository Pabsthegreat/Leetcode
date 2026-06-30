"""
[Description]
Number of Substrings Containing All Three Characters
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 
Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:

Input: s = "abc"
Output: 1

 
Constraints:

  3 <= s.length <= 5 x 10^4
  s only consists of a, b or c characters.

[Metadata]
- Difficulty: Medium
- Topics: Hash Table, String, Sliding Window
- Slug: number-of-substrings-containing-all-three-characters
"""

// [Solution]
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        l = 0
        ans = 0

        for r in range(len(s)):
            count[s[r]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += len(s) - r
                count[s[l]] -= 1
                l += 1

        return ans