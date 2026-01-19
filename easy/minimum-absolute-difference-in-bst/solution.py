"""
[Description]
Minimum Absolute Difference in BST
https://leetcode.com/problems/minimum-absolute-difference-in-bst/

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

 
Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1

 
Constraints:

  The number of nodes in the tree is in the range [2, 104].
  0 <= Node.val <= 105

 
Note: This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

[Metadata]
- Difficulty: Easy
- Topics: Tree, Depth-First Search, Breadth-First Search, Binary Search Tree, Binary Tree
- Slug: minimum-absolute-difference-in-bst
"""

// [Solution]
class Solution(object):
    def getMinimumDifference(self, root):
        self.prev = None
        self.min_diff = float('inf')
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
            
        inorder(root)
        return self.min_diff