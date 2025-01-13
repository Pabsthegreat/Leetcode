//Linked List
//Math
//Recursion

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    int carry = 0;
    struct ListNode* head = NULL;
    struct ListNode* pres = NULL;

    while (l1 != NULL || l2 != NULL) {
        int sum = carry;
        
        if (l1 != NULL) {
            sum += l1->val;
            l1 = l1->next;
        }
        
        if (l2 != NULL) {
            sum += l2->val;
            l2 = l2->next;
        }
        
        carry = sum / 10;
        struct ListNode* temp = (struct ListNode*)malloc(sizeof(struct ListNode));
        temp->val = sum % 10;
        temp->next = NULL;
        
        if (head == NULL) {
            head = temp;
            pres = head;
        } else {
            pres->next = temp;
            pres = pres->next;
        }
    }
    if (carry > 0) {
        struct ListNode* temp = (struct ListNode*)malloc(sizeof(struct ListNode));
        temp->val = carry;
        temp->next = NULL;
        pres->next = temp;
    }

    return head;
}
