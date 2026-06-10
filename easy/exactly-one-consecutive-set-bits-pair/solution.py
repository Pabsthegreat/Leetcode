"""
[Description]
Exactly One Consecutive Set Bits Pair
https://leetcode.com/problems/exactly-one-consecutive-set-bits-pair/

You are given an integer n.

Return true if its binary representation contains exactly one pair of consecutive set bits, and false otherwise.

 
Example 1:

Input: nums = 6

Output: true

Explanation:

  Binary representation of 6 is 110.
  There is exactly one pair of consecutive set bits ("11"). Thus, the answer is true​​​​​​​.

Example 2:

Input: nums = 5

Output: false

Explanation:

  Binary representation of 5 is 101.
  There are no consecutive set bits. Thus, the answer is false​​​​​​​.

 
Constraints:

  0 <= n <= 105

[Metadata]
- Difficulty: Easy
- Topics: 
- Slug: exactly-one-consecutive-set-bits-pair
"""

// [Solution]
class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        s = 1
        count = 0
        prev = -1
        while n:
            b = n%2
            if b == 1:
                if s == 1:
                    s -= 1
                    prev = 1
                elif s == 0 and prev == 1:
                    count += 1
                    prev = 1
                else:
                    prev = 1
            else:
                s = 1
                prev = 0
            n = n//2
        if count == 1:
            return True
        else:
            return False