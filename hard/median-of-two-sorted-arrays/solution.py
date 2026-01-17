"""
[Description]
Median of Two Sorted Arrays
https://leetcode.com/problems/reverse-integer/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 
Constraints:

  nums1.length == m
  nums2.length == n
  0 <= m <= 1000
  0 <= n <= 1000
  1 <= m + n <= 2000
  -106 <= nums1[i], nums2[i] <= 106

[Metadata]
- Difficulty: Hard
- Topics: Array, Binary Search, Divide and Conquer
- Slug: median-of-two-sorted-arrays
"""

// [Solution]
class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        INT_MAX = 2**31 - 1  # 2147483647

        while x:
            pop = x % 10
            x //= 10
            # If rev will exceed INT_MAX after *10 + pop, return 0
            if rev > (INT_MAX - pop) // 10:
                return 0

            rev = rev * 10 + pop

        return sign * rev