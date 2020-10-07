class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 가장 적은 개수의 코인으로 바꾸기
        
        # dp 테이블 초기화
        answer = [amount+1] * (amount+1)
        answer[0] = 0
        
        # 1부터 amount까지 각 숫자마다 최소의 개수를 찾음
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    # 값 i를 가장 적은 개수로 표현할 수 있는 것으로 다시 할당
                    answer[i] = min(answer[i], answer[i-c] + 1)
        
        return answer[-1] if answer[-1] != amount+1 else -1
