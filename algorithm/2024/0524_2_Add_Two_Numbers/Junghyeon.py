class Solution:
    def addTwoNumbers(self, l1, l2):
        # 리스트 시작 부분 정의
        tail = ptr = ListNode(0)
        ptr.next = tail
        num = 0
        
        # 남아있는 리스트에서 값을 더함
        while l1 or l2:
            ptr = ptr.next            
            n = num
            if l1:
                n += l1.val
                l1 = l1.next
            if l2:
                n += l2.val
                l2 = l2.next
            
            ptr.val = n % 10
            num = n // 10
            ptr.next = ListNode(0)
        
        if num:
            ptr = ptr.next
            ptr.val = num
        
        ptr.next = None
        
        return tail
