# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        answer = ListNode()
        temp = answer
        Up = 0 # 자릿수 올림을 위한 변수
        while(l1 != None or l2 != None): # 모든 list가 끝날때 까지 반복
            # 두 노드중 비어있는 노드가 있는 경우 0으로 할당함
            if l1 == None:
                l1 = ListNode()
            if l2 == None:
                l2 = ListNode()
            temp.val += (l1.val + l2.val+ Up) % 10
            Up = (l1.val + l2.val+ Up) / 10
            l1, l2 = l1.next, l2.next
                        
            if l1 == None and l2 == None:
                if Up == 0:
                    break
                else:
                    temp.next = ListNode()
                    temp.next.val = Up
                    break
            temp.next = ListNode()
            temp = temp.next
            
        return answer        
