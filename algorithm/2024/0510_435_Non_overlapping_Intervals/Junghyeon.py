# 가장 큰 수를 기준으로 
class Solution:
    def eraseOverlapIntervals(self, intervals):
        # 끝나는 수를 기준으로 정렬
        intervals.sort(key=lambda x: x[1])
        
        cnt = 0
        max_num = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < max_num:
                # 현재 시작 interval이 이전의 끝나는 interval보다 작으면 카운트
                cnt += 1
            else:
                # max_num 업데이트
                max_num = intervals[i][1]
        
        return cnt
