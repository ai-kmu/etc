class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 시작점에 대해 오름차순으로, 끝점에 대해 내림차순으로 정렬
        sorted_intervals = sorted(intervals, key = lambda x : (x[0], -x[1]))
        count = 0
        end = 0

        # interval의 끝점이 end보다 크다면 count 업데이트
        for interval in sorted_intervals:
            if interval[1] > end:
                count += 1
                end = interval[1]

        return count
