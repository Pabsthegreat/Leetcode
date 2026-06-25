"""
[Description]
Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 
Example 1:

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

 
Constraints:

  1 <= preorder.length <= 3000
  inorder.length == preorder.length
  -3000 <= preorder[i], inorder[i] <= 3000
  preorder and inorder consist of unique values.
  Each value of inorder also appears in preorder.
  preorder is guaranteed to be the preorder traversal of the tree.
  inorder is guaranteed to be the inorder traversal of the tree.

[Metadata]
- Difficulty: Medium
- Topics: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
- Slug: construct-binary-tree-from-preorder-and-inorder-traversal
"""

// [Solution]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        inorder_index = {}

        for i, val in enumerate(inorder):
            inorder_index[val] = i

        self.pre_idx = 0

        def build(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            mid = inorder_index[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)