class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        timeSeries.sort()
        poisoned = duration

        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i - 1] < duration:
                poisoned += (timeSeries[i] - timeSeries[i - 1])

            else:
                poisoned += duration

        return poisoned
