"""
[Description]
Permutations
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:
Input: nums = [1]
Output: [[1]]

 
Constraints:

  1 <= nums.length <= 6
  -10 <= nums[i] <= 10
  All the integers of nums are unique.

[Metadata]
- Difficulty: Medium
- Topics: Array, Backtracking
- Slug: permutations
"""

// [Solution]
class Solution(object):
    def permute(self, nums):
        res = []
        curr = []
        used = set()

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for num in nums:
                if num in used:
                    continue

                curr.append(num)
                used.add(num)

                backtrack()

                curr.pop()
                used.remove(num)

        backtrack()
        return res