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
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in ind:
                return [ind[complement], i] 
            
            ind[nums[i]] = i
        
        return None