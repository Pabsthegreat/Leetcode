"""
[Description]
Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 
Example 1:

Input: head = [1,1,2]
Output: [1,2]

Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

 
Constraints:

  The number of nodes in the list is in the range [0, 300].
  -100 <= Node.val <= 100
  The list is guaranteed to be sorted in ascending order.

[Metadata]
- Difficulty: Easy
- Topics: Linked List
- Slug: remove-duplicates-from-sorted-list
"""

// [Solution]
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head

        # Traverse the list
        while curr and curr.next:
            # If current value equals next value, skip next node
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head