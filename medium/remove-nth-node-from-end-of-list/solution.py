"""
[Description]
Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.

 
Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

 
Constraints:

  The number of nodes in the list is sz.
  1 <= sz <= 30
  0 <= Node.val <= 100
  1 <= n <= sz

 
Follow up: Could you do this in one pass?

[Metadata]
- Difficulty: Medium
- Topics: Linked List, Two Pointers
- Slug: remove-nth-node-from-end-of-list
"""

// [Solution]
class Solution:
    def removeNthFromEnd(self, head, n):
        arr = []
        curr = head

        while curr:
            arr.append(curr)
            curr = curr.next

        length = len(arr)
        remove_index = length - n

        if remove_index == 0:
            return head.next

        arr[remove_index - 1].next = arr[remove_index].next

        return head