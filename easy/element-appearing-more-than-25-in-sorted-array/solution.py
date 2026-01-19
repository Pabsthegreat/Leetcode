"""
[Description]
Element Appearing More Than 25% In Sorted Array
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 
Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:

Input: arr = [1,1]
Output: 1

 
Constraints:

  1 <= arr.length <= 104
  0 <= arr[i] <= 105

[Metadata]
- Difficulty: Easy
- Topics: Array
- Slug: element-appearing-more-than-25-in-sorted-array
"""

// [Solution]
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) <=3 :
            return arr[0]
        s = list(sorted(arr))
        le = len(arr)
        p1 = s[0:int(le/4)]
        p2 = s[int(le/4):int(le/2)]
        p3 = s[int(le/2):int(le*3/4)]
        p4 = s[int(le*3/4):]
        l = [p1,p2,p3,p4]
        i = 0
        while i < 3:
            s1 = set(l[i])
            if len(s1) == 1 and s.count(list(s1)[0]) > le/4:
                return list(s1)[0]
            else:
                if l[i][-1] == l[i+1][0] and s.count(l[i][-1]) > le/4:
                    return l[i][-1]
            i+= 1
        if p4[0] == p3[-1] and len(set(p4)) == 1:
            return p4[0]
        else:
            if len(set(p4)) == 1 and s.count(p4[0])>le/4:
                return p4[0]
    