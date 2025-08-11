class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # 예외 케이스
        if num == 1:
            return False

        # 1은 무조건 있으니까 포함되기도 하고
        # 현 알고리즘으로는 1을 넣으면 본인도 들어가서 꼬이기 때문에 제외
        summ = 1

        # 탐색은 루트까지만 하면 됨
        for i in range(2, floor(num ** 0.5) + 1):
            # 나누어 떨어지지 않으면 패스
            if num % i:
                continue
            
            # 나누어 떨어지면 그 값과
            summ += i
            # 대칭 값을 넣되, 동일할 수도 있으니 (제곱수) 체크 필요
            if i != (num //i):
                summ += (num // i)
        
        return summ == num
