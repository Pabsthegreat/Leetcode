/*
[Description]
Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 
Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

 
Constraints:

  The number of nodes in both lists is in the range [0, 50].
  -100 <= Node.val <= 100
  Both list1 and list2 are sorted in non-decreasing order.

[Metadata]
- Difficulty: Easy
- Topics: Linked List, Recursion
- Slug: merge-two-sorted-lists
*/

// [Solution]
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* create(struct ListNode* head, int data) {
    struct ListNode* temp = (struct ListNode*)malloc(sizeof(struct ListNode));
    temp->next = NULL;
    temp->val = data;
    if (head == NULL) {
        head = temp;
    } else {
        struct ListNode* pres = head;
        while (pres->next != NULL) {
            pres = pres->next;
        }
        pres->next = temp;
    }
    return head;
}

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode* head = NULL;

    while (list1 != NULL && list2 != NULL) {
        if (list1->val <= list2->val) {
            head = create(head, list1->val);
            list1 = list1->next;
        } else {
            head = create(head, list2->val);
            list2 = list2->next;
        }
    }

    // If any elements are left in either list, append them to the result
    while (list1 != NULL) {
        head = create(head, list1->val);
        list1 = list1->next;
    }
    
    while (list2 != NULL) {
        head = create(head, list2->val);
        list2 = list2->next;
    }

    return head;
}