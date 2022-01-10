class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # binary search와 DP의 결합
        
        # day를 입력으로 주면 days에서 해당 day 바로 직전의 것의 index를 return
        def binary_search(day):
            start, end = 0, len(days)-1
            
            while start <= end:
                mid = (start + end) // 2
                
                if days[mid] == day:
                    return mid-1
                elif days[mid] < day:
                    start = mid + 1
                else:
                    end = mid - 1
            return end
        
        # cost를 저장하는 배열
        # base case: 0번째 위치의 값이 0 
        #            => 0일동안 여행하는 데 드는 비용이 0이라는 뜻
        # i = {1 ~ len(day)}일 때,
        # dp[i] = days[i-1]동안 여행하는데 드는 최소 비용
        dp = [0] * (len(days)+1)
        
        for i in range(1, len(days)+1):
            day = days[i-1]
            # 현재 day를 마지막으로 하는 일주일권을 끊었다고 가정함
            # 해당 일주일권에 포함하지 않는 day들 중 마지막 day의 index를 binary search로 찾음
            # +1하는 이유는 days와 dp의 index가 서로 1만큼 차이나기 때문
            # 만약 현재 day 이전의 모든 day들을 포함한다고 하면,
            # binary_search(day-6)는 -1을 return하고 seven_days_ago는 0이 됨
            # dp[0] = 0이기 때문에 문제 없이 작동
            seven_days_ago = binary_search(day-6) + 1
            # 한달권도 마찬가지
            thirty_days_ago = binary_search(day-29) + 1
            
            # 현재 day의 cost는 다음 값들중의 최솟값과 같다.
            # 1. 하루권을 끊는 경우 => 이전 cost를 더한다.
            # 2. 일주일권을 끊는 경우 => 일주일권에 포함시킬수 있는 최근 이전 day들을 제외시키고 남은 day의 cost를 더한다.
            # 3. 한달권을 끊는 경우 => 일주일권과 마찬가지
            cost = min(dp[i-1] + costs[0], dp[seven_days_ago] + costs[1], dp[thirty_days_ago] + costs[2]) # seven_days_ago, thirty_days_ago index값을 이진 탐색으로 찾아냄.
            
            dp[i] = cost
        
        return dp[-1]
            
