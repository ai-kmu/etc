class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        return duration + sum([duration if timeSeries[i] - timeSeries[i - 1] > duration else timeSeries[i] - timeSeries[i - 1] for i in range(1, len(timeSeries))])
