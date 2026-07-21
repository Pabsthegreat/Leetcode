"""
[Description]
Permutations II
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 
Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

 
Constraints:

  1 <= nums.length <= 8
  -10 <= nums[i] <= 10

[Metadata]
- Difficulty: Medium
- Topics: Array, Backtracking, Sorting
- Slug: permutations-ii
"""

// [Solution]
class Solution(object):
    def permuteUnique(self, nums):
        curr = []
        res = []
        n = {i: nums.count(i) for i in nums}
        l = len(nums)

        def backtrack():
            if len(curr) == l:
                res.append(curr[:])
                return

            for i in n:
                if not n[i]:
                    continue

                curr.append(i)
                n[i] -= 1
                backtrack()
                n[i] += 1
                curr.pop()

        backtrack()
        return res