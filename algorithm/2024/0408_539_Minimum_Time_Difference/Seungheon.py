class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        timePoints.sort()

        time_list = [ int(tp[:2]) * 60 + int(tp[3:]) for tp in timePoints]

        answer = min(abs(time_list[-1] - time_list[0]), abs(time_list[-1] - time_list[0] - 60 * 24))

        for i, t in enumerate(time_list[:-1]):
            answer = min(abs(time_list[i+1] - time_list[i]), answer)

        return answer
