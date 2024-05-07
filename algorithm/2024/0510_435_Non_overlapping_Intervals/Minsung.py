class Solution:
    def eraseOverlapIntervals(self, intervals):
        '''
        intervals[i] = [start_i, end_i]
        sorted : end 기준으로 오름차순 정렬
        last_dest : 가장 최근 도착지
        '''
        intervals = sorted(intervals, key = lambda x : x[1])  
        ans = 0
        last_dest = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= last_dest:  
                last_dest = end
            else:  # 현재 시작점이 마지막 도착지보다 작다면 overlapping -> 제거
                ans += 1
        return ans
