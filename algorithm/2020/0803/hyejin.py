class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        first_node = ''
        second_node = ''
        
        # 첫번째 linked list의 값을 string으로 만들기
        while l1 != None:
            first_node += str(l1.val)
            l1 = l1.next
        # 두번째 linked list의 값을 string으로 만들기
        while l2 != None:
            second_node += str(l2.val)
            l2 = l2.next
        
        # 두 string을 반대로 뒤집음
        first_node = first_node[::-1]
        second_node = second_node[::-1]
        
        # 더하기
        answer = int(first_node) + int(second_node)
        
        # 마지막부터 linked list에 넣기
        first = ListNode()
        output = first
        while answer != 0:
            val = answer % 10
            answer = answer//10
            output.val = val
            if answer == 0:
                break
            output.next = ListNode()
            output = output.next
            
        return first    
