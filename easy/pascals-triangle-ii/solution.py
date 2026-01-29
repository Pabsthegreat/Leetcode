"""
[Description]
Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:
Input: rowIndex = 0
Output: [1]
Example 3:
Input: rowIndex = 1
Output: [1,1]

 
Constraints:

  0 <= rowIndex <= 33

 
Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

[Metadata]
- Difficulty: Easy
- Topics: Array, Dynamic Programming
- Slug: pascals-triangle-ii
"""

// [Solution]
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        i = 2
        l = [1,1]
        while i < rowIndex+1:
            temp = [1]
            for j in range(0,len(l)-1):
                temp.append(l[j]+l[j+1])
            temp.append(1)
            l = temp
            i+=1
        return l
            