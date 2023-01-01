from collections import deque

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # DP 테이블과 큐 초기화
        # 무조건 첫 번째 인덱스가 들어가야 함
        q = deque([0])
        dp = [0] * n
        dp[0] = nums[0]
        # 1번째 인덱스부터 끝까지 순회하면서
        for i in range(1, n):
            # print(q)
            # 큐가 점프 범위를 넘어가면 뺌
            if q and q[0] < i - k:
                q.popleft()
            # 현재 점프할 위치에서 현재 인덱스의 점수가 더해진 값이 들어감
            dp[i] = dp[q[0]] + nums[i]
            # q에 저장된 dp값이 현재 dp값보다 클 때까지 pop
            while q and dp[i] >= dp[q[-1]]:
                q.pop()
            # 현재 dp의 인덱스를 q에 추가
            q.append(i)
        # print(q)
        # print(dp)
        return dp[-1]
