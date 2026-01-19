"""
[Description]
Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 
Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

 
Constraints:

  1 <= points.length <= 300
  points[i].length == 2
  -104 <= xi, yi <= 104
  All the points are unique.

[Metadata]
- Difficulty: Hard
- Topics: Array, Hash Table, Math, Geometry
- Slug: max-points-on-a-line
"""

// [Solution]
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 2:
            return n
            
        m = 0
        for i in range(n):
            s = {}
            same_point = 0  # Handle duplicate points
            for j in range(i+1, n):
                # Handle duplicate points
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same_point += 1
                    continue
                    
                # Calculate slope
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0:
                    slope = float('inf')  # Vertical line
                else:
                    slope = float(dy) / float(dx)  # Ensure float division
                    
                s[slope] = s.get(slope, 0) + 1
            
            # Current point + duplicates + max collinear points
            current_max = same_point + 1  # At least the point itself + duplicates
            if s:
                current_max += max(s.values())
            m = max(m, current_max)
            
        return m