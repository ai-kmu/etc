

class Solution { 
    public: ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) { 
        ListNode *c1 = l1, *c2 = l2, *head = nullptr, *prev = nullptr; 
        short c = 0; 
        while(c1 || c2 || c){ 
            c += (c1 ? c1->val : 0);
            c += (c2 ? c2->val : 0);
            ListNode *cur = new ListNode(c % 10);
            c /= 10; 
            if(!head) head = cur; 
            if(prev) prev->next = cur;
            prev = cur;
            if(c1) c1 = c1->next; 
            if(c2) c2 = c2->next; 
        } 
        return head; 
    } 
};
