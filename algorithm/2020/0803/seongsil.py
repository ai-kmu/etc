# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = l1
        y = l2
        first = []
        second = []
        while x:  # ListNode 리스트로 받기
            first.append(x.val)
            x = x.next
        while y:
            second.append(y.val)
            y = y.next
        
        first.reverse()  
        second.reverse()
        
        new_first = "".join(map(str, first))
        new_second = "".join(map(str, second))
        
        result = str(int(new_first) + int(new_second))  # 리스트로 결과 저장
        
        result_to_list = [x for x in result]
        result_to_list.reverse()
    
        l3 = ListNode(result_to_list.pop())   # 리스트 -> ListNode

        for i in reversed(result_to_list):
            l3 = ListNode(i, l3)
       
        return l3
