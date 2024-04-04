class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()  # 시간순으로 정렬

        min_ = 24 * 60

        for i in range(len(timePoints)):  # 첫번째, 마지막 값 비교까지 포함하여 반복
            h1, m1 = map(int, timePoints[i - 1].split(":"))
            h2, m2 = map(int, timePoints[i].split(":"))
            time_diff = ((h2 - h1) * 60 + m2 - m1) % (24 * 60)
            min_ = min(min_, time_diff)

        return min_
