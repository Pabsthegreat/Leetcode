"""
[Description]
Binary Tree Postorder Traversal
https://leetcode.com/problems/binary-tree-postorder-traversal/

Given the root of a binary tree, return the postorder traversal of its nodes' values.

 
Example 1:

Input: root = [1,null,2,3]

Output: [3,2,1]

Explanation:

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,6,7,5,2,9,8,3,1]

Explanation:

Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]

 
Constraints:

  The number of the nodes in the tree is in the range [0, 100].
  -100 <= Node.val <= 100

 
Follow up: Recursive solution is trivial, could you do it iteratively?

[Metadata]
- Difficulty: Easy
- Topics: Stack, Tree, Depth-First Search, Binary Tree
- Slug: binary-tree-postorder-traversal
"""

// [Solution]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        out = []
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            out.append(root.val)
        postorder(root)
        return out