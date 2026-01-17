"""
[Description]
Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

  The left subtree of a node contains only nodes with keys strictly less than the node's key.
  The right subtree of a node contains only nodes with keys strictly greater than the node's key.
  Both the left and right subtrees must also be binary search trees.

 
Example 1:

Input: root = [2,1,3]
Output: true

Example 2:

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

 
Constraints:

  The number of nodes in the tree is in the range [1, 104].
  -231 <= Node.val <= 231 - 1

[Metadata]
- Difficulty: Medium
- Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree
- Slug: validate-binary-search-tree
"""

// [Solution]
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ind = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in ind:
                return [ind[complement], i] 
            
            ind[nums[i]] = i
        
        return None