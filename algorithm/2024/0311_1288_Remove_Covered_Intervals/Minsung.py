class Solution:
    
    def removeCoveredIntervals(self, intervals):
        
        intervals.sort(key = lambda x : (x[0], -x[1])) # left가 같다면 right이 큰 것 부터 
        # last_right : 가장 최근에 기록한 interval의 끝 
        last_right = intervals[0][1] # 첫 시작은 ans에 포함
        ans = 1

        for left, right in intervals[1:]: # 첫 시작은 포함시켰으므로 두 번째부터 check
            
            if left > last_right: # 마지막 interval의 끝보다 시작이 크다면 포함
                last_right = right # 마지막 interval의 끝 갱신 
                ans += 1 # 포함시켜야 하므로 답 + 1
            
            elif left <= last_right and right > last_right: # 시작이 마지막 interval 끝 이전이지만 끝이 이후라면 포함 시켜야 함
                last_right = right # 마지막 interval의 끝 갱신
                ans += 1 # 포함시켜야 하므로 답 + 1
        
        return ans
