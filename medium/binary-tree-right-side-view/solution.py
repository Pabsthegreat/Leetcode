"""
[Description]
Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

 
Example 1:

Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:

Example 2:

Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:

Example 3:

Input: root = [1,null,3]

Output: [1,3]

Example 4:

Input: root = []

Output: []

 
Constraints:

  The number of nodes in the tree is in the range [0, 100].
  -100 <= Node.val <= 100

[Metadata]
- Difficulty: Medium
- Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- Slug: binary-tree-right-side-view
"""

// [Solution]
from collections import deque
from typing import List, Optional

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            level = []
            size = len(q)

            for i in range(size):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level[-1])

        return res