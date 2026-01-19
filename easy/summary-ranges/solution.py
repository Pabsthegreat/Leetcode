"""
[Description]
Summary Ranges
https://leetcode.com/problems/summary-ranges/

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

  "a->b" if a != b
  "a" if a == b

 
Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

 
Constraints:

  0 <= nums.length <= 20
  -231 <= nums[i] <= 231 - 1
  All the values of nums are unique.
  nums is sorted in ascending order.

[Metadata]
- Difficulty: Easy
- Topics: Array
- Slug: summary-ranges
"""

// [Solution]
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        r = []
        start = nums[0]
        j = 1
        end = start
        for i in nums[1:]:
            if i == start + j:
                j+=1
                end = i
                continue
            else:
                if start == end:
                    r += [str(start)]
                    j = 1
                    start = i
                    end = start
                else:
                    r += [str(start)+"->"+str(end)]
                    j = 1
                    start = i
                    end = start
        if start == end:
            r += [str(start)]
        else:
            r  += [str(start)+"->"+str(end)]
        return r

            