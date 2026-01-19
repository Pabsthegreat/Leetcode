"""
[Description]
Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

  There is no string in strs that can be rearranged to form "bat".
  The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
  The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 
Constraints:

  1 <= strs.length <= 104
  0 <= strs[i].length <= 100
  strs[i] consists of lowercase English letters.

[Metadata]
- Difficulty: Medium
- Topics: Array, Hash Table, String, Sorting
- Slug: group-anagrams
"""

// [Solution]
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        l = []
        d = {}
        c = 0
        for i in strs:
            s = "".join(sorted(i))
            if s not in d:
                d[s] = c
                c+=1
                l.append([i])
            else:
                l[d[s]].append(i)
        return l
