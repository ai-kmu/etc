class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        idx = 0
        last = timeSeries[0]
        
        for time in timeSeries[1:]:
            if last + duration - 1 < time:
                idx += duration
            else:
                idx += time - last
            last = time

        idx += duration

        return idx
