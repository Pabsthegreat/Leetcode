"""
[Description]
Sort List
https://leetcode.com/problems/sort-list/

Given the head of a linked list, return the list after sorting it in ascending order.

 
Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:

Input: head = []
Output: []

 
Constraints:

  The number of nodes in the list is in the range [0, 5 * 104].
  -105 <= Node.val <= 105

 
Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

[Metadata]
- Difficulty: Medium
- Topics: Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
- Slug: sort-list
"""

// [Solution]
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        # find middle of list
        fast = head
        slow = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # split list into 2 halves
        prev.next = None

        left = head
        right = slow

        l = self.sortList(left)
        r = self.sortList(right)

        return self.merge(l, r)

    def merge(self, l, r):
        dummy = ListNode(0)
        curr = dummy

        while l and r:
            if l.val <= r.val:
                curr.next = l
                l = l.next
            else:
                curr.next = r
                r = r.next

            curr = curr.next

        if l:
            curr.next = l
        else:
            curr.next = r

        return dummy.next