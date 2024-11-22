class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        
        answer = 0
        for t_i, t in enumerate(timeSeries):
            # 마지막
            if t_i == len(timeSeries) - 1:
                answer += duration
            else:
                answer += min(timeSeries[t_i+1]-timeSeries[t_i], duration)
        
        return answer
