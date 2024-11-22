class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        before = 0
        tot = 0
        for v, i in enumerate(timeSeries):
            tot += duration
            dup = i - (before + duration)
            before = i
            if v == 0:
                continue
            # 겹침
            if dup < 0:
                tot += dup
        return tot
