"""
[Description]
Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 
Constraints:

  The number of nodes in the tree is in the range [0, 2000].
  -1000 <= Node.val <= 1000

[Metadata]
- Difficulty: Medium
- Topics: Tree, Breadth-First Search, Binary Tree
- Slug: binary-tree-level-order-traversal
"""

// [Solution]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        curr = [root] #use deque to reduce space but interating a evolving list not recommended
        res = [[root.val]]
        while curr:
            t = []
            v = []
            for i in curr:
                if i.left:
                    t.append(i.left)
                    v.append(i.left.val)
                if i.right:
                    t.append(i.right)
                    v.append(i.right.val)
            curr = t
            if v:
                res.append(v)
            else:
                break
        return res