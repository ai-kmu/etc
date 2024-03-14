class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
            count = 0  # 겹치는 간격 수
            right = 0  # 현재까지 탐색한 구간 중 가장 오른쪽 끝점

            # start 값을 기준으로 정렬, start 값이 같은 경우 end 값을 기준으로 정렬
            # ex) [[1, 4], [3, 6], [2, 8], [3, 7]] => [[1, 4], [2, 8], [3, 7], [3, 6]]
            intervals.sort(key=lambda x: (x[0], -x[1]))

            for start, end in intervals:
                if end > right:  # 선택된 구간이 이전 구간과 겹치지 않는 경우
                    right = end  # 현재 구간의 end 값을 right에 저장
                else:  # 선택된 구간이 이전 구간과 겹치는 경우
                    count += 1  # 겹치는 간격 수 + 1

            return len(intervals) - count
