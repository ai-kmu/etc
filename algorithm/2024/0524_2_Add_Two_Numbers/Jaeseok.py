# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        # 자리수 올림 확인을 위한 flag
        flag = False
        # 현재 자리수를 나타내는 커서 역할
        cur = answer
        while True:
            # 더할 수가 None이면 더할 것이 없으므로 0 저리
            val_1 = l1.val if l1 is not None else 0
            val_2 = l2.val if l2 is not None else 0
            # 자리수 올림이 있으면 1을 더해주고 flag 처리, 없으면 그냥 더해줌
            if flag == True:
                now_val = val_1 + val_2 + 1
                flag = False
            else:
                now_val = val_1 + val_2
            # 더한 값이 10을 넘기면 flag 처리하고 10으로 나눈 나머지만 현재 자리수에 남김
            if now_val >= 10:
                now_val %= 10
                flag = True
            cur.val = now_val
            # 더할 수 있는 데까지 더해주기 위해 각 수를 다음으로 옮김
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            # 만약 두 수를 더할 수 있는 데 까지 더했고 올림할 자리수도 없다면 탈출
            if l1 is None and l2 is None and flag != True:
                break
            # 아니라면 결과값의 커서를 다음으로 옮겨줌
            cur.next = ListNode()
            cur = cur.next
        return answer
        
