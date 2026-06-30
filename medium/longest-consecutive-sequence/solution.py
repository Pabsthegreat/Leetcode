"""
[Description]
Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 
Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:

Input: nums = [1,0,1,2]
Output: 3

 
Constraints:

  0 <= nums.length <= 105
  -109 <= nums[i] <= 109

[Metadata]
- Difficulty: Medium
- Topics: Array, Hash Table, Union-Find
- Slug: longest-consecutive-sequence
"""

// [Solution]
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            # Only start from the beginning of a sequence
            if num - 1 not in nums_set:
                current = num
                length = 1

                while current + 1 in nums_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest
        