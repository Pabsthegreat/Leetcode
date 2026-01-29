"""
[Description]
Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:
Input: numRows = 1
Output: [[1]]

 
Constraints:

  1 <= numRows <= 30

[Metadata]
- Difficulty: Easy
- Topics: Array, Dynamic Programming
- Slug: pascals-triangle
"""

// [Solution]
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        i = 2
        l = [[1],[1,1]]
        while i < numRows:
            temp = [1]
            for j in range(0,len(l[i-1])-1):
                temp.append(l[i-1][j]+l[i-1][j+1])
            temp.append(1)
            l.append(temp)
            i+=1
        return l
            

