"""
[Description]
Count Binary Substrings
https://leetcode.com/problems/count-binary-substrings/

Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

 
Example 1:

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

 
Constraints:

  1 <= s.length <= 105
  s[i] is either '0' or '1'.

[Metadata]
- Difficulty: Easy
- Topics: Two Pointers, String
- Slug: count-binary-substrings
"""

// [Solution]
class Solution(object):
    def countBinarySubstrings(self, s):
        groups = []
        count = 1
        
        # Step 1: Count consecutive character groups
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)  # Don't forget the last group
        
        # Step 2: Sum min of adjacent groups
        result = 0
        for i in range(len(groups) - 1):
            result += min(groups[i], groups[i+1])
        
        return result