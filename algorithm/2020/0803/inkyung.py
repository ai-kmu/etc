class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = '', ''  # 입력받은 l1과 l2를 숫자로 표현하기 위한 변수
        while l1.next:       # l1.next가 없을때까지 l1.val를 str타입으로 저장하고 l1을 l1.next로 초기화
            num1 += str(l1.val)
            l1 = l1.next
        num1 += str(l1.val)  # 마지막 l1에는 l1.val만 있고 l1.next가 없으므로 l1.val만 한번더 추가하기
          
        while l2.next:       # l1과 같은 방식으로 진행
            num2 += str(l2.val)
            l2 = l2.next
        num2 += str(l2.val)
        num = str(int(num1[::-1]) + int(num2[::-1])). # num1과num2에 저장된 str타입을 뒤집어서 숫자로 바꾼 후 더한 다음에 다시 str로 변환해서 ListNode에 입력

        answer = ListNode(num[0]) # 첫번째 숫자가 정답을 제일 안쪽 ListNode의 val로 추가됨
        for i in range(1, len(num)):  # 이후 ListNode에 각각 val값과 next값으로 저장하면서 반복하기 
            answer = ListNode(num[i], answer)

        return answer
