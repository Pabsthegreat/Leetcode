"""
[Description]
Angle Between Hands of a Clock
https://leetcode.com/problems/angle-between-hands-of-a-clock/

Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.

 
Example 1:

Input: hour = 12, minutes = 30
Output: 165

Example 2:

Input: hour = 3, minutes = 30
Output: 75

Example 3:

Input: hour = 3, minutes = 15
Output: 7.5

 
Constraints:

  1 <= hour <= 12
  0 <= minutes <= 59

[Metadata]
- Difficulty: Medium
- Topics: Math
- Slug: angle-between-hands-of-a-clock
"""

// [Solution]
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h_per_hr = 360 / 12      # 30 degrees per hour
        h_per_min = h_per_hr / 60 # 0.5 degrees per minute
        m_per_min = 360 / 60     # 6 degrees per minute

        total_h = h_per_hr * hour + minutes * h_per_min
        total_m = m_per_min * minutes

        diff = abs(total_h - total_m)

        return min(diff, 360 - diff)