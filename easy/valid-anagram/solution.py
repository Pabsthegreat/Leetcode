"""
[Description]
Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 
Constraints:

  1 <= s.length, t.length <= 5 * 104
  s and t consist of lowercase English letters.

 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

[Metadata]
- Difficulty: Easy
- Topics: Hash Table, String, Sorting
- Slug: valid-anagram
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