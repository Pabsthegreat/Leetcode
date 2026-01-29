"""
[Description]
Meeting Rooms
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

 
Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true

 
Constraints:

  0 <= intervals.length <= 104
  intervals[i].length == 2
  0 <= starti < endi <= 106

[Metadata]
- Difficulty: Easy
- Topics: Array, Sorting
- Slug: meeting-rooms
"""

// [Solution]
class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        intervals.sort(key = lambda x:x[0])
        if not intervals:
            return True
        end = intervals[0][1]
        for i in intervals[1:]:
            if i[0] >= end:
                end = i[1]
            else:
                return False
        return True
