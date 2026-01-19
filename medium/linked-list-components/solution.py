"""
[Description]
Linked List Components
https://leetcode.com/problems/linked-list-components/

You are given the head of a linked list containing unique integer values and an integer array nums that is a subset of the linked list values.

Return the number of connected components in nums where two values are connected if they appear consecutively in the linked list.

 
Example 1:

Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] and [3] are the two connected components.

Example 2:

Input: head = [0,1,2,3,4], nums = [0,3,1,4]
Output: 2
Explanation: 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.

 
Constraints:

  The number of nodes in the linked list is n.
  1 <= n <= 104
  0 <= Node.val < n
  All the values Node.val are unique.
  1 <= nums.length <= n
  0 <= nums[i] < n
  All the values of nums are unique.

[Metadata]
- Difficulty: Medium
- Topics: Array, Hash Table, Linked List
- Slug: linked-list-components
"""

// [Solution]
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: ListNode
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)  # Use a set for O(1) lookups
        count = 0
        in_component = False
        
        while head:
            if head.val in num_set:
                if not in_component:
                    # We found the start of a new component
                    count += 1
                    in_component = True
            else:
                in_component = False  # End of a component
                
            head = head.next
        
        return count