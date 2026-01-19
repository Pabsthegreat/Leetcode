"""
[Description]
Maximum Score After Splitting a String
https://leetcode.com/problems/maximum-score-after-splitting-a-string/

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 
Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:

Input: s = "1111"
Output: 3

 
Constraints:

  2 <= s.length <= 500
  The string s consists of characters '0' and '1' only.

[Metadata]
- Difficulty: Easy
- Topics: String, Prefix Sum
- Slug: maximum-score-after-splitting-a-string
"""

// [Solution]
class Solution:
    def maxScore(self, s: str) -> int:
        o = [0]
        z = [0]
        l = len(s) - 1

        # Compute cumulative counts
        for i in range(len(s)):
            if s[i] == "0":
                z.append(z[-1] + 1)
            else:
                z.append(z[-1])

            if s[l - i] == "1":
                o.append(o[-1] + 1)
            else:
                o.append(o[-1])

        # Reverse the `o` array and slice `z` correctly
        z = z[1:]
        o = o[::-1]

        # Calculate the maximum score
        m = 0
        for i in range(len(z) - 1):  # Split points are from 0 to len(s)-2
            if o[i + 1] + z[i] > m:
                m = o[i + 1] + z[i]
        return m
