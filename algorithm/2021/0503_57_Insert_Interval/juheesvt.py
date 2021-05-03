class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        # newInterval이 다른 interval과 비교되면서 업데이트되므로, mergeInterval
        mergedInterval = newInterval
        left, right = [], []

        for interval in intervals:
            if interval[1] < mergedInterval[0]:
                left += interval,
            elif interval[0] > mergedInterval[1]:
                right += interval,
            else:
                mergedInterval[0] = min(mergedInterval[0], interval[0])
                mergedInterval[1] = max(mergedInterval[1], interval[1])
        
        # 최종 결과는 [left] + mergedInterval + [right]
        return left + [mergedInterval] + right
