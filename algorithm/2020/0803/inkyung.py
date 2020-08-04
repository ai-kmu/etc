class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = '', ''
        while l1.next:
            num1 += str(l1.val)
            l1 = l1.next
        num1 += str(l1.val)
          
        while l2.next:
            num2 += str(l2.val)
            l2 = l2.next
        num2 += str(l2.val)
        num = str(int(num1[::-1]) + int(num2[::-1]))

        answer = ListNode(num[0])
        for i in range(1, len(num)):
            answer = ListNode(num[i], answer)

        return answer
