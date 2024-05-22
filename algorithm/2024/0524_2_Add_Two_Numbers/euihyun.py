# 풀다가 정답 봤습니다. 리뷰 안해주셔도 됩니다

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer_lst = ListNode() 
        curr_answer = answer_lst 
        
        curr_l1 = l1 
        curr_l2 = l2
        
        while True:
        	# 첫번째, 두번째 리스트 비었으면 그만
            if not curr_l1 and not curr_l2:
                break
            
            # 전 노드에서 10 넘으면 1 받아주기
            _sum = curr_answer.val
            
            # 첫번째 리스트 안비었으면 더하고 다음노드
            if curr_l1:
                _sum += curr_l1.val
                curr_l1 = curr_l1.next
              
            if curr_l2:
                _sum += curr_l2.val
                curr_l2 = curr_l2.next
            
            # 현재 정답 노드의 값이
            remainder = _sum % 10
            
            #  뒤로 넘겨줄 수
            share = _sum // 10
            
            curr_answer.val = remainder
            
            if share or curr_l1 or curr_l2:
                curr_answer.next = ListNode(share)  
                curr_answer = curr_answer.next
        
        return answer_lst
