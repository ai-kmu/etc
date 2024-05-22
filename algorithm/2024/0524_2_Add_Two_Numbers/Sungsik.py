# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp_node = ListNode(val=None, next=None)
        root = tmp_node
        
        q, r = divmod(l1.val + l2.val, 10)
        tmp_node.val = r
        tmp_q = q
        
        while l1.next or l2.next:
            if l1.next:
                l1 = l1.next
                val1 = l1.val
            else:
                val1 = 0
            if l2.next:
                l2 = l2.next
                val2 = l2.val
            else:
                val2 = 0
            
            # l1과 l2와 이전 자리수에서 올라온 값을 더함
            q, r = divmod(val1 + val2 + tmp_q, 10)
            tmp_node.next = ListNode(val=r, next=None)
            tmp_node = tmp_node.next
            
            tmp_q = q
        
        # 다 끝나고 올라온 값이 있으면 이를 추가
        if tmp_q:
            tmp_node.next = ListNode(val=tmp_q, next=None)
        return root
            
            
            
