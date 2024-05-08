# 못풀고 답지 봤습니다.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        point = intervals[0][-1]
        cnt = 0
        for start, end in intervals[1:]:
            if start >= point:
                point = end                
                continue
            else:
                if end <= point:
                    cnt += 1
                    point = end
                else:
                    cnt += 1
        return cnt
