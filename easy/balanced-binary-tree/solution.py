"""
[Description]
Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

 
Constraints:

  The number of nodes in the tree is in the range [0, 5000].
  -104 <= Node.val <= 104

[Metadata]
- Difficulty: Easy
- Topics: Tree, Depth-First Search, Binary Tree
- Slug: balanced-binary-tree
"""

// [Solution]
class Solution(object):
    def isBalanced(self, root):
        def getHeight(node):
            # Base case: empty tree has height 0
            if node is None:
                return 0
            
            # Get heights of left and right subtrees
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            
            # If any subtree is unbalanced, propagate -1
            if left_height == -1 or right_height == -1:
                return -1
            
            # If current node is unbalanced, return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return height of current node
            return max(left_height, right_height) + 1
        
        return getHeight(root) != -1