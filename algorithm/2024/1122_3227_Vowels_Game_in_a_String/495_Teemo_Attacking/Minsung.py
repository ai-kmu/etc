class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        poisoned = [[timeSeries[0], timeSeries[0]+duration-1]]  # [start, end]
        for i in timeSeries[1:]:
            if i > poisoned[-1][1]:
                poisoned.append([i, i+duration-1])
            if i <= poisoned[-1][1]:
                poisoned[-1][1] = i+duration-1
        for start, end in poisoned:
            ans += end-start+1
        return ans
