"""
[Description]
Binary Tree Vertical Order Traversal
https://leetcode.com/problems/binary-tree-vertical-order-traversal/

Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]

Example 2:

Input: root = [3,9,8,4,0,1,7]
Output: [[4],[9],[3,0,1],[8],[7]]

Example 3:

Input: root = [1,2,3,4,10,9,11,null,5,null,null,null,null,null,null,null,6]
Output: [[4],[2,5],[1,10,9,6],[3],[11]]

 
Constraints:

  The number of nodes in the tree is in the range [0, 100].
  -100 <= Node.val <= 100

[Metadata]
- Difficulty: Medium
- Topics: Hash Table, Tree, Depth-First Search, Breadth-First Search, Sorting, Binary Tree
- Slug: binary-tree-vertical-order-traversal
"""

// [Solution]
from collections import deque, defaultdict

class Solution(object):
    def verticalOrder(self, root):
        if not root:
            return []
        
        # Dictionary: {column: [values in that column]}
        col_table = defaultdict(list)
        
        # Queue: (node, column)
        queue = deque([(root, 0)])
        
        while queue:
            node, col = queue.popleft()
            
            # Add node value to its column
            col_table[col].append(node.val)
            
            # Add children with their columns
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        
        # Sort by column and return values
        return [col_table[col] for col in sorted(col_table.keys())]