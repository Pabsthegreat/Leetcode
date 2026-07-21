"""
[Description]
Can Place Flowers
https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 
Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

 
Constraints:

  1 <= flowerbed.length <= 2 * 104
  flowerbed[i] is 0 or 1.
  There are no two adjacent flowers in flowerbed.
  0 <= n <= flowerbed.length

[Metadata]
- Difficulty: Easy
- Topics: Array, Greedy
- Slug: can-place-flowers
"""

// [Solution]
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 0
        i = 0
        while i < len(flowerbed):
            if flowerbed[i]:
                i += 2  # skip next plot (guaranteed empty)
            else:
                if (i == 0 or not flowerbed[i-1]) and (i == len(flowerbed) - 1 or not flowerbed[i+1]):
                    c += 1
                    i += 2
                else:
                    i += 1
            if c >= n:
                return True
        return c >= n