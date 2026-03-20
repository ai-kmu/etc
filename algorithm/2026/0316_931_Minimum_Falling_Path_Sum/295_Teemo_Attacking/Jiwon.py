class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # ans = set()

        # for i in timeSeries:
        #     ans |= set(range(i, i + duration))

        # return len(ans)
        # 시간 초과 ㅡㅡ
      
        ans = 0

        for i in range(len(timeSeries) - 1):
            ans += min(timeSeries[i + 1] - timeSeries[i], duration)

        return ans + duration
