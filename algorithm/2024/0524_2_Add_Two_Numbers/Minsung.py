# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.reversed_ListNode_to_str(l1)
        l2 = self.reversed_ListNode_to_str(l2)
        ans = l1 + l2
        ans = str(ans)[::-1]  # ListNode를 만들기 위해 역순 처리
        answer = ListNode(val = ans[0], next = None if len(ans) == 1 else ListNode())
        
        cur = answer.next
        for i, val in enumerate(ans[1:]):
            cur.val = val
            if i == len(ans) - 2:
                cur.next = None
            else:
                cur.next = ListNode()
            cur = cur.next

        return answer
    
    def reversed_ListNode_to_str(self, n):
        '''
        문제에서 주어진 거꾸로 된 ListNode type 객체를 하나의 int로 나타내는 함수
        :type n: ListNode
        :rtype: int
        '''
        list_n = list()
        while n:
            list_n.append(n.val)
            n = n.next
        n = int(''.join(list(map(str, list_n)))[::-1])  # 역순을 처리함과 동시에 하나의 int로 표현
        return n
