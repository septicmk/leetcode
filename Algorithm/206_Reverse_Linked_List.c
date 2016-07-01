/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode * ret = NULL;
    while(head != NULL){
        struct ListNode *tmp = head;
        head = head->next;
        tmp->next = ret;
        ret = tmp;
    }
    return ret;
}
