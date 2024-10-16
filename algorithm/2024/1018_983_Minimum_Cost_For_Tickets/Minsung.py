class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        '''
        costs[0] : 1-day
        costs[1] : 7-day
        costs[2] : 30-day

        BFS & DP
            - bfs
                - [0]: 현재 날짜
                - [1]: 현재까지 사용한 비용
            - dp
                - key: day
                - value: cost
                - day까지 도달하는데 최소 cost 저장
        '''
        next_days = [1, 7, 30]
        from collections import deque
        q = deque()
        q.append([days[0], 0]) 
        dp = dict()
        ans = 1e9
        while q:
            cur_day, cur_cost = q.popleft()  # 탐색에 사용할 현재 날짜와 비용
            try:
                if dp[cur_day] <= cur_cost:  # 현재 비용이 dp에 저장된 최소 비용보다 높으면 탐색 X
                    continue
            except:
                pass  # 현재 날짜를 처음 탐색할 시 pass
            dp[cur_day] = cur_cost  
            for i, next_cost in enumerate(costs):
                next_day = cur_day + next_days[i]
                next_cost = cur_cost + next_cost
                if next_day > days[-1]:  # 정답에는 최솟값 저장
                    ans = min(ans, next_cost)
                q.append([self.appropriate_day(days, next_day), next_cost])
        return ans
    
    def appropriate_day(self, days, target):
        '''
        binray search 이용
        
        return 'days 안 value 중, target 이상이며 최소값'
        '''
        left = 0
        right = len(days) - 1
        min_day = days[-1]
        while left <= right:
            mid = (left+right) // 2
            if days[mid] < target:
                left = mid + 1
            else:
                min_day = min(min_day, days[mid])
                right = mid - 1
        return min_day
                
