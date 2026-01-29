"""
[Description]
Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/

Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 
Example 1:

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]

Example 2:

Input: root = [1]
Output: ["1"]

 
Constraints:

  The number of nodes in the tree is in the range [1, 100].
  -100 <= Node.val <= 100

[Metadata]
- Difficulty: Easy
- Topics: String, Backtracking, Tree, Depth-First Search, Binary Tree
- Slug: binary-tree-paths
"""

// [Solution]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        if not root:
            return []
        
        result = []
        
        def dfs(node, path):
            # Add current node to path
            if path:
                path += "->" + str(node.val)
            else:
                path = str(node.val)
            
            # If leaf node, add path to result
            if not node.left and not node.right:
                result.append(path)
                return
            
            # Recurse on children if they exist
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)
        
        dfs(root, "")
        return result