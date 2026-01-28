"""
[Description]
Symmetric Tree
https://leetcode.com/problems/symmetric-tree/editorial/

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 
Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false

 
Constraints:

  The number of nodes in the tree is in the range [1, 1000].
  -100 <= Node.val <= 100

 
Follow up: Could you solve it both recursively and iteratively?

[Metadata]
- Difficulty: Easy
- Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- Slug: symmetric-tree
"""

// [Solution]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        
        def mirror(right,left):
            if not right and not left:
                return True

            if not left or not right:
                return False
            
            return (mirror(left.left, right.right)) and left.val == right.val and mirror(left.right, right.left)

        return mirror(root.right, root.left)