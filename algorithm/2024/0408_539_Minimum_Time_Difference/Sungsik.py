class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 분으로 변환
        minutes = sorted([int(x[:2]) * 60 + int(x[3:]) for x in timePoints])
        minutes.append(minutes[0] + 1440)
        # 차이 중 가장 작은 것을 return
        return min([y - x for x, y in zip(minutes[:-1], minutes[1:])])
