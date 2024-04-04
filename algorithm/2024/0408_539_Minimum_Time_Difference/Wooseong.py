class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # str을 분 단위의 숫자로 변경
        def str_to_min(t):
            h, m = t.split(":")
            return int(h) * 60 + int(m)
        
        # 숫자 배열로 변경 후 정렬
        times = [str_to_min(t) for t in timePoints]
        times.sort()
        n = len(times)
        
        # 가능한 최댓값은 1440
        ans = 1440
        # 순차적으로 업데이트
        for i in range(n - 1):
            ans = min(ans, times[i + 1] - times[i])
        # 마지막으로 처음과 끝값으로 업데이트
        ans = min(ans, times[0] - times[-1] + 1440)
        
        return ans
