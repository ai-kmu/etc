class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # DP 문제
        # 우선 여행하는 일수의 총 길이 + 1만큼 DP 테이블을 만들어줌
        max_day = days[-1]
        dp = [0] * (max_day + 1)
        index = 0
        for i, _ in enumerate(dp):
            # 만약 현재 DP 인덱스가 여행하는 날짜라면 하루치, 7일치, 30일치를 샀을 때 최소 비용을 구함
            # option : 총 여행일이 30일이 넘지 않는 경우, 7일을 넘지 않는 경우에도 패스는 살 수 있으므로 그럴 때는 인덱스를 0으로
            # index : 현재 dp 테이블이 days에 있는 여행 일자와 동일한지 확인, 같다면 다음 일자를 찾아감
            if i == days[index]:
                index += 1
                option_1 = i - 30 if i >= 30 else 0
                option_2 = i - 7 if i >= 7 else 0
                dp[i] = min(dp[option_1] + costs[2], dp[option_2] + costs[1], dp[i-1] + costs[0])
            # dp 테이블의 일자가 days의 일자와 일치하지 않으면 어제까지의 최소 비용을 그대로 사용
            else:
                dp[i] = dp[i-1]
        # 최종 비용을 리턴
        return dp[-1]
        
