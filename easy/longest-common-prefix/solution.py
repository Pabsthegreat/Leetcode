"""
[Description]
Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 
Constraints:

  1 <= strs.length <= 200
  0 <= strs[i].length <= 200
  strs[i] consists of only lowercase English letters if it is non-empty.

[Metadata]
- Difficulty: Easy
- Topics: Array, String, Trie
- Slug: longest-common-prefix
"""

// [Solution]
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        c= ""
        for i,s in enumerate(strs[0]):
            for k in strs[1:]:
                if k[0:i+1] != strs[0][0:i+1]:
                    return c
            c += s
        return c
        