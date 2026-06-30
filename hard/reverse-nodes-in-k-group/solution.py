"""
[Description]
Reverse Nodes in k-Group
https://leetcode.com/problems/reverse-nodes-in-k-group/

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 
Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Example 2:

Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

 
Constraints:

  The number of nodes in the list is n.
  1 <= k <= n <= 5000
  0 <= Node.val <= 1000

 
Follow-up: Can you solve the problem in O(1) extra memory space?

[Metadata]
- Difficulty: Hard
- Topics: Linked List, Recursion
- Slug: reverse-nodes-in-k-group
"""

// [Solution]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        # count length
        le = 0
        node = head
        while node:
            le += 1
            node = node.next

        prev = dummy
        curr = head

        while curr and le >= k:
            conn = None
            tail = curr   # after reversal, curr becomes the tail of this group

            tl = k
            while tl:
                temp = curr.next
                curr.next = conn
                conn = curr
                curr = temp
                tl -= 1

            # connect previous part to reversed group
            prev.next = conn

            # connect tail of reversed group to remaining list
            tail.next = curr

            # move prev to tail
            prev = tail

            le -= k

        return dummy.next