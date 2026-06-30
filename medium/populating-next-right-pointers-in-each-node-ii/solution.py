"""
[Description]
Populating Next Right Pointers in Each Node II
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 
Example 1:

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.

Example 2:

Input: root = []
Output: []

 
Constraints:

  The number of nodes in the tree is in the range [0, 6000].
  -100 <= Node.val <= 100

 
Follow-up:

  You may only use constant extra space.
  The recursive approach is fine. You may assume implicit stack space does not count as extra space for this problem.

[Metadata]
- Difficulty: Medium
- Topics: Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
- Slug: populating-next-right-pointers-in-each-node-ii
"""

// [Solution]
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        def find(node):
            temp = node.next

            while temp:
                if temp.left:
                    return temp.left
                elif temp.right:
                    return temp.right
                else:
                    temp = temp.next

            return None

        def dfs(node):
            if not node:
                return

            # Case 1: both children exist
            if node.left and node.right:
                node.left.next = node.right

            # Case 2: connect right child to next available child
            if node.right:
                node.right.next = find(node)

            # Case 3: if no right child, connect left child directly
            elif node.left:
                node.left.next = find(node)

            # Important: process right before left
            dfs(node.right)
            dfs(node.left)

        root.next = None
        dfs(root)
        return root