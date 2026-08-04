"""
[Description]
Longest Subarray of 1's After Deleting One Element
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 
Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

 
Constraints:

  1 <= nums.length <= 105
  nums[i] is either 0 or 1.

[Metadata]
- Difficulty: Medium
- Topics: Array, Dynamic Programming, Sliding Window
- Slug: longest-subarray-of-1s-after-deleting-one-element
"""

// [Solution]
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ma = 0
        prev = None
        cur= 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
            else:
                if prev is None:
                    prev = i
                else:
                    ma = max(cur,ma)
                    cur = i-prev-1
                    prev = i
        if prev is None:
            return max(ma,cur) - 1
        else:
            return max(ma,cur)