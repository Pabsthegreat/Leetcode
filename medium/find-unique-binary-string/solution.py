"""
[Description]
Find Unique Binary String
https://leetcode.com/problems/find-unique-binary-string/

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

 
Example 1:

Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:

Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:

Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

 
Constraints:

  n == nums.length
  1 <= n <= 16
  nums[i].length == n
  nums[i] is either '0' or '1'.
  All the strings of nums are unique.

[Metadata]
- Difficulty: Medium
- Topics: Array, Hash Table, String, Backtracking
- Slug: find-unique-binary-string
"""

// [Solution]
class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        n = len(nums)
        s = set()
        s.update({"0"*n, "1"*n})
        for i in nums:
            o = i.count("1")
            m = "1"*(n-o) + "0"*o
            p = "0"*(n-o) + "1"*o
            s.update({m,p,m[::-1],p[::-1]})
        s2 = list(s-set(nums))
        if s2 == []:
            return "1"* int(n/2) + "0"*int(n/2)
        else:
            return s2[0]