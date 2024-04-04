class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # 시간을 분으로 바꿔서 timePoints에 다시 저장
        for i, v in enumerate(timePoints):
            timePoints[i] = int(v[0:2]) * 60 + int(v[3:5])
        # 내림차순으로 timePoints sort
        timePoints.sort(reverse=True)
        # 시간(분) 순서대로 정렬했기 때문에 가장 차이가 큰 시간이 실제로 가장 작은 경우를 고려
        # ex) 00:00 -> 24:00으로 고려한 뒤 차이 계산
        answer = 1440 + timePoints[-1] - timePoints[0]
        # 나머지 시간들은 일반적인 분 차이로 최솟값을 찾아줌
        for i in range(len(timePoints) - 1):
            res = timePoints[i] - timePoints[i + 1]
            answer = min(res, answer)
        return answer
