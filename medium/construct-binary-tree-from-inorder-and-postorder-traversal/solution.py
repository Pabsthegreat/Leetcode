"""
[Description]
Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

 
Example 1:

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]

 
Constraints:

  1 <= inorder.length <= 3000
  postorder.length == inorder.length
  -3000 <= inorder[i], postorder[i] <= 3000
  inorder and postorder consist of unique values.
  Each value of postorder also appears in inorder.
  inorder is guaranteed to be the inorder traversal of the tree.
  postorder is guaranteed to be the postorder traversal of the tree.

[Metadata]
- Difficulty: Medium
- Topics: Array, Hash Table, Divide and Conquer, Tree, Binary Tree
- Slug: construct-binary-tree-from-inorder-and-postorder-traversal
"""

// [Solution]
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_val = {}

        for i, val in enumerate(inorder):
            inorder_val[val] = i

        self.post_ord_idx = len(postorder) - 1

        def build(left, right):
            if left > right:
                return None

            root_val = postorder[self.post_ord_idx]
            self.post_ord_idx -= 1

            root = TreeNode(root_val)

            mid = inorder_val[root_val]

            #here
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root #imp

        return build(0, len(inorder) - 1)