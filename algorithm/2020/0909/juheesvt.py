class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        if len(intervals) <2:
            return intervals
        
        first = intervals[0]
        result = []
        for interval in intervals:
            if interval[0] > first[1]:
                result.append(first)
                first = interval
            else :
                first[1]= max(first[1],interval[1])
        result.append(first)
        return result
