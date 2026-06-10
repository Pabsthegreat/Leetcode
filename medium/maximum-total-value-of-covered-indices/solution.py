"""
[Description]
Maximum Total Value of Covered Indices
https://leetcode.com/problems/maximum-total-value-of-covered-indices/

You are given an integer array nums of length n and a binary string s of length n, where s[i] == '1' means index i initially contains a token and s[i] == '0' means it does not.

You may perform the following operation any number of times:

  Choose a token currently located at index i, where i > 0, such that this token has not been moved before.
  Move this token from index i to index i - 1.

An index is considered covered if it contains a token after all moves.

Return an integer denoting the maximum total value of nums at the covered indices after optimally performing the operations.

 
Example 1:

Input: nums = [9,2,6,1], s = "0101"

Output: 15

Explanation:

  Initially, indices 1 and 3 contain tokens.
  Move the token from index 3 to index 2.
  Move the token from index 1 to index 0.
  The covered indices are [0, 2], so the total value is nums[0] + nums[2] = 9 + 6 = 15.

Example 2:

Input: nums = [5,1,4], s = "001"

Output: 4

Explanation:

  Initially, only index 2 contains a token.
  It is optimal to leave the token at index 2.
  The covered index is [2], so the total value is nums[2] = 4.

Example 3:

Input: nums = [9,3,5], s = "011"

Output: 14

Explanation:

  Initially, indices 1 and 2 contain tokens.
  Move the token from index 1 to index 0.
  The covered indices are [0, 2], so the total value is nums[0] + nums[2] = 9 + 5 = 14.

 
Constraints:

  1 <= n == nums.length == s.length <= 105
  1 <= nums[i] <= 105
  ​​​​​​​s[i] is either '0' or '1'

[Metadata]
- Difficulty: Medium
- Topics: 
- Slug: maximum-total-value-of-covered-indices
"""

// [Solution]
class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        total = 0
        n = len(nums)
        i = 0
        while i < n:
            while i <n and s[i] == '0':
                i += 1
            l = i

            while i<n and s[i]=='1':
                i+= 1
            r = i-1

            if l == 0:
                total += sum(nums[l:r+1])
            else:
                total += sum(nums[l-1:r+1]) - min(nums[l-1:r+1])
                
        return total