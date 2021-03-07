# 곱이 가장 큰 경우
# n = 몫*나누는 수 + 나머지
# 몫이 1 이상인 경우에
# 나머지가 1 이상인 경우 -> (몫+1) 곱하기
# 나머지가 0인 경우 -> (몫) 곱하기
# 그 중 가장 큰 경우가 정답

class Solution:
    def integerBreak(self, n: int) -> int:
        d_num = 2                            # 2부터 시작
        answer = 0                           
        while n // d_num > 0:                # (n/나누는 수)의 몫이 0이 될 떄까지
            share = n // d_num               # 몫
            remainer = n % d_num             # 나머지
            out = 1
            for i in range(d_num):           # 나누는 수 만큼
                if remainer != 0:            # 나머지가 0이 아니라면
                    out *= share+1           # 몫에 1을 더해 곱하기
                    remainer -= 1            # 나머지 1 감소
                else:
                    out *= share             # 나머지가 없는 경우 몫을 그대로 곱하기
            if answer < out:
                answer = out
            d_num += 1                       # 나누는 수 1 증가
        return answer
