class Solution:
    def findPoisonedDuration(self, t: List[int], d: int) -> int:
        return d+sum(min(t[i+1]-t[i], d) for i in range(len(t)-1))
