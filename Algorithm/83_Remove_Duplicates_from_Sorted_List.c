/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (head == NULL) return head;
    struct ListNode* ret = head;
    while(head->next != NULL){
        if (head->val == head->next->val){
            head->next = head->next->next;
        }else{
            head = head->next;
        }
    }
    return ret;
}
