from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        current = dummy_head
        carry = 0
        
        # 두 리스트가 모두 없어질 때까지 반복
        while l1 or l2:
            # 두 노드의 값과 carry 더하기
            total_sum = carry
            if l1:
                total_sum += l1.val
                l1 = l1.next
            if l2:
                total_sum += l2.val
                l2 = l2.next
            
            carry = total_sum // 10
            
            current.next = ListNode(total_sum % 10)
            current = current.next
        
        # 마지막 덧셈 후에 남아 있는 carry가 있는 경우
        if carry > 0:
            current.next = ListNode(carry)
        
        # dummy_head의 다음 노드를 반환
        return dummy_head.next
