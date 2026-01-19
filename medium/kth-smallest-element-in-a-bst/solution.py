"""
[Description]
Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 
Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

 
Constraints:

  The number of nodes in the tree is n.
  1 <= k <= n <= 104
  0 <= Node.val <= 104

 
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

[Metadata]
- Difficulty: Medium
- Topics: Tree, Depth-First Search, Binary Search Tree, Binary Tree
- Slug: kth-smallest-element-in-a-bst
"""

// [Solution]
class Solution(object):
    def kthSmallest(self, root, k):
        stack = []
        current = root
        
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            k -= 1
            if k == 0:
                return current.val
            current = current.right

# class Solution(object):
#     def kthSmallest(self, root, k):
#         """
#         :type root: Optional[TreeNode]
#         :type k: int
#         :rtype: int
#         """
#         self.count = 0
#         self.result = None
        
#         def dfs(node):
#             if not node or self.result is not None:
#                 return
#             dfs(node.left)
#             self.count += 1
#             if self.count == k:
#                 self.result = node.val
#                 return
#             dfs(node.right)
            
#         dfs(root)
#         return self.result