class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1]))
        temp = intervals[0][1]
        ret = 0

        for s, e in intervals[1:]:
            if s < temp and e <= temp:
                ret += 1
                temp = e

            elif s < temp and e > temp:
                ret += 1

            else:
                temp = e

        return ret
