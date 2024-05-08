class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        _, prev_y = intervals[0]
        answer = 0
        
        for x, y in intervals[1:]:
            # 겹치는 경우
            if x < prev_y:
                # 겹치는 interval중 하나를 지워야 한다.
                # 그 중 오른쪽 값이 작은걸 지우는 것이 이득
                prev_y = min(prev_y, y)
                answer += 1
            else:
                prev_y = y
        
        return answer
        
