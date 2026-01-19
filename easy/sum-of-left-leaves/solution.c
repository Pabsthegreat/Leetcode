/*
[Description]
Sum of Left Leaves
https://leetcode.com/problems/sum-of-left-leaves/

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 
Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:

Input: root = [1]
Output: 0

 
Constraints:

  The number of nodes in the tree is in the range [1, 1000].
  -1000 <= Node.val <= 1000

[Metadata]
- Difficulty: Easy
- Topics: Tree, Depth-First Search, Breadth-First Search, Binary Tree
- Slug: sum-of-left-leaves
*/

// [Solution]
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int sumOfLeftLeaves(struct TreeNode* root) {
    if (root == NULL) {
        return 0;
    }
    int c = 0;
    if (root->left != NULL && root->left->left == NULL && root->left->right == NULL) {
        c += root->left->val;
    }
    c += sumOfLeftLeaves(root->left);
    c += sumOfLeftLeaves(root->right);

    return c;
}
