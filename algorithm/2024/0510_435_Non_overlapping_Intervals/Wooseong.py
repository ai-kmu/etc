class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 아무튼 끝나는 지점이 짧아야 덜 겹침
        intervals.sort(key=lambda x: x[1])

        # end는 이전에 가장 늦게 끝났던 지점 저장
        answer = 0
        end = -65535
        
        # 시작 지점이 끝 지점보다 크다면 안 겹치는 거임
        # 작다면, 끝 지점 기준으로 sort된 상태이기 때문에 겹치는 거임
        for left, right in intervals:
            if left >= end:
                end = right
            else:
                answer += 1

        return answer
