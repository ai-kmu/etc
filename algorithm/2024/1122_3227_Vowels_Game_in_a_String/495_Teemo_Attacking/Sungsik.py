class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        timeSeries.append(1000000000)
        answer = 0
        
        for prev, new in zip(timeSeries[:-1], timeSeries[1:]):
            answer += min(new - prev, duration)
        
        return answer
