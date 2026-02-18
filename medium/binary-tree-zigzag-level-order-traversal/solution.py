"""
[Description]
Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 
Constraints:

  The number of nodes in the tree is in the range [0, 2000].
  -100 <= Node.val <= 100

[Metadata]
- Difficulty: Medium
- Topics: Tree, Breadth-First Search, Binary Tree
- Slug: binary-tree-zigzag-level-order-traversal
"""

// [Solution]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        lvl = [[root.val]]
        curr = [root]
        d = False
        while curr:
            print(d)
            t = []
            v = []
            for i in curr:
                if i.left:
                    t.append(i.left)
                    v.append(i.left.val)
                if i.right:
                    t.append(i.right)
                    v.append(i.right.val)
            if t:
                if d == True:
                    lvl.append(v)
                else:
                    lvl.append(v[::-1])
            else:
                break

            curr = t #level order means bfs always from left to right dont flip this, only the values
            d = not d
        return lvl
