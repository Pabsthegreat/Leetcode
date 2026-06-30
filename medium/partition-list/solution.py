"""
[Description]
Partition List
https://leetcode.com/problems/partition-list/

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 
Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

 
Constraints:

  The number of nodes in the list is in the range [0, 200].
  -100 <= Node.val <= 100
  -200 <= x <= 200

[Metadata]
- Difficulty: Medium
- Topics: Linked List, Two Pointers
- Slug: partition-list
"""

// [Solution]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)

        small = small_dummy
        big = big_dummy

        curr = head

        while curr:
            nxt = curr.next
            curr.next = None

            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                big.next = curr
                big = big.next

            curr = nxt

        small.next = big_dummy.next

        return small_dummy.next