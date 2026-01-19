"""
[Description]
Rotate List
https://leetcode.com/problems/rotate-list/

Given the head of a linked list, rotate the list to the right by k places.

 
Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]

 
Constraints:

  The number of nodes in the list is in the range [0, 500].
  -100 <= Node.val <= 100
  0 <= k <= 2 * 109

[Metadata]
- Difficulty: Medium
- Topics: Linked List, Two Pointers
- Slug: rotate-list
"""

// [Solution]
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # Count nodes
        n = 0
        t = head
        while t:
            n += 1
            t = t.next
        
        m = k % n
        if m == 0:
            return head
        
        # Find new tail (at position n - m - 1)
        new_tail = head
        for _ in range(n - m - 1):
            new_tail = new_tail.next
        
        # New head is next node
        new_head = new_tail.next
        new_tail.next = None  # Break the list
        
        # Connect old tail to old head
        t = new_head
        while t.next:
            t = t.next
        t.next = head
        
        return new_head