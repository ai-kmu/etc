class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        insert = newInterval
        start = len(intervals)
        end = len(intervals)
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        for idx, interval in enumerate(intervals):
            if interval[0] <= newInterval[0] and newInterval[0] <= interval[1]:
                start = idx
                insert[0] = interval[0]
            elif idx == 0 and newInterval[0] < interval[0]:
                start = idx
                insert[0] = newInterval[0]
            elif idx != 0 and intervals[idx-1][1] < newInterval[0] and newInterval[0] < interval[0]:
                start = idx
                insert[0] = newInterval[0]
            if interval[0] <= newInterval[1] and newInterval[1] <= interval[1]:
                end = idx
                insert[1] = interval[1]
            elif idx == 0 and newInterval[1] < interval[0]:
                end = idx
                insert[1] = newInterval[1]
            elif idx != 0 and intervals[idx-1][1] < newInterval[1] and newInterval[1] < interval[0]:
                end = idx-1
                insert[1] = newInterval[1]
        return intervals[:start] + [insert] + intervals[end+1:]
