class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = duration

        for i in range(len(timeSeries) - 1):
            
            if timeSeries[i+1] - timeSeries[i] > duration:
                answer += duration
            else:
                answer += timeSeries[i+1] - timeSeries[i]


        return answer
