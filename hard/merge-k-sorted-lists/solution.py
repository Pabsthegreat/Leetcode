"""
[Description]
Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

 
Constraints:

  k == lists.length
  0 <= k <= 104
  0 <= lists[i].length <= 500
  -104 <= lists[i][j] <= 104
  lists[i] is sorted in ascending order.
  The sum of lists[i].length will not exceed 104.

[Metadata]
- Difficulty: Hard
- Topics: Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
- Slug: merge-k-sorted-lists
"""

// [Solution]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l,r):
            dummy = ListNode(0)
            if not l or not r:
                return l or r
            if l.val > r.val:
                dummy.next = r
                r = r.next
            else:
                dummy.next = l
                l = l.next
            head = dummy.next
            while l and r:
                if l.val > r.val:
                    head.next = r
                    r = r.next
                else:
                    head.next = l
                    l = l.next
                head = head.next
            if not l:
                head.next = r
            else:
                head.next = l
            return dummy.next

        def build(l,r):
            if l > r:
                return None
            if l == r:
                return lists[l]
            mid = (l+r)//2
            
            left = build(l,mid)
            right = build(mid+1,r)

            return merge(left,right)
        return build(0,len(lists)-1)