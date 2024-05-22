# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp = 0
        temp1 = l1
        temp2 = l2
        ret = ListNode(temp1.val + temp2.val)
        temp1 = temp1.next
        temp2 = temp2.next
        temp_ret = ret

        while temp1 and temp2:
            temp_listNode = ListNode(temp_ret.val // 10 + temp1.val + temp2.val)
            temp_ret.val = temp_ret.val % 10
            temp_ret.next = temp_listNode
            temp_ret = temp_listNode
            temp1 = temp1.next
            temp2 = temp2.next

        while temp1:
            temp_listNode = ListNode(temp_ret.val // 10 + temp1.val)
            temp_ret.val = temp_ret.val % 10
            temp_ret.next = temp_listNode
            temp_ret = temp_listNode
            temp1 = temp1.next

        while temp2:
            temp_listNode = ListNode(temp_ret.val // 10 + temp2.val)
            temp_ret.val = temp_ret.val % 10
            temp_ret.next = temp_listNode
            temp_ret = temp_listNode
            temp2 = temp2.next

        if temp_ret.val > 9:
            temp_listNode = ListNode(temp_ret.val // 10)
            temp_ret.val = temp_ret.val % 10
            temp_ret.next = temp_listNode
            temp_ret = temp_listNode

        return ret
        

        
        
        
