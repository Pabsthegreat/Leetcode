"""
[Description]
Left and Right Sum Differences
https://leetcode.com/problems/left-and-right-sum-differences/

You are given a 0-indexed integer array nums of size n.

Define two arrays leftSum and rightSum where:

  leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
  rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

Return an integer array answer of size n where answer[i] = |leftSum[i] - rightSum[i]|.

 
Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

 
Constraints:

  1 <= nums.length <= 1000
  1 <= nums[i] <= 105

[Metadata]
- Difficulty: Easy
- Topics: Array, Prefix Sum
- Slug: left-and-right-sum-differences
"""

// [Solution]
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = len(nums)-1
        left_sum = 0
        right_sum = 0
        ans = [0]*(l+1)
        for i in range(l+1):
            ans[i] = abs(left_sum - ans[i])
            ans[l-i] = abs(ans[l-i] - right_sum)
            left_sum+=nums[i]
            right_sum+=nums[l-i]
        return ans