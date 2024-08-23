class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        # 큰거 두개씩 지우기
        answer = 0
        
        while True:
            amount.sort()
            if 0 == amount[-1]:
                return answer
            else:
                if 0 != amount[-2]:
                    amount[-2] -= 1
                amount[-1] -= 1
                answer += 1
        return answer

