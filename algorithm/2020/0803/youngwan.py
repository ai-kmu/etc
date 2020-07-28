class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = 0
        mul = 1
        while l1.next:                # l1을 숫자로 바꿔 num1에 저장
            num1 += l1.val*mul
            mul *= 10
            l1 = l1.next
        num1 += l1.val*mul
        
        num2 = 0
        mul = 1
        while l2.next:                # l2를 숫자로 바꿔 num2에 저장
            num2 += l2.val*mul
            mul *= 10
            l2 = l2.next
        num2 += l2.val*mul
            
        num = num1 + num2             # 두 숫자를 더하고
        
        number = list(str(num))       # 더한 숫자를 str로 바꿔
        a = ListNode(int(number[0]))  # 가장 높은 자리 수부터 linked list에 저장
        for i in range(1, len(number)):  
            a = ListNode(number[i], a)
        return a
