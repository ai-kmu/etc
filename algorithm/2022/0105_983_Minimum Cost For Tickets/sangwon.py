class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # 날짜마다 3가지 선택이 있다.
        # day1 day7 day30 pass 중 하나 선택
        # day7은 1부터 7일까지 여행 가능
        # 최소 비용 구하기
        # 인덱스로 접근할 것이다.
        # dfs를 이용
        dp = {}

        def dfs(i):
            if i == len(days):  # basecase를 정의 마지막날을 연산하면 끝
                return 0
            if i in dp:
                return dp[i]  # 범위안에 있는 경우 계속 호출
            dp[i] = float("inf")
            for d, c in zip([1, 7, 30], costs):
                # 날짜와 날짜에 해당하는 가격을 zip으로 하나로 묶는다.
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    # 7일이나 30일을 구매할 때 구매한 날짜로 부터 7days나 30days를 더했을때 초과안할 때까지 j더하기
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
                # 현재 구매한 날짜수의 가격과 7일이나 30일을 추가한 가격을 비교
            return dp[i]

        return dfs(0)
