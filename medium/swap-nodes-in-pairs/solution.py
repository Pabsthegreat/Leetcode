"""
[Description]
Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/

Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 
Example 1:

Input: head = [1,2,3,4]

Output: [2,1,4,3]

Explanation:

Example 2:

Input: head = []

Output: []

Example 3:

Input: head = [1]

Output: [1]

Example 4:

Input: head = [1,2,3]

Output: [2,1,3]

 
Constraints:

  The number of nodes in the list is in the range [0, 100].
  0 <= Node.val <= 100

[Metadata]
- Difficulty: Medium
- Topics: Linked List, Recursion
- Slug: swap-nodes-in-pairs
"""

// [Solution]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next

            # swap
            a.next = b.next
            b.next = a
            prev.next = b

            # move prev to end of swapped pair
            prev = a

        return dummy.next