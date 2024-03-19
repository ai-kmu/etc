class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        answer = 0
        end = 0
        # sort
        # 1. 왼쪽이 작은 순으로 정렬
        # 2. 오른쪽이 큰 순으로 정렬
        # -> 현재 end 기준으로 오른쪽이 크면 새로운 interval
        # ex)
        # [[1, 4], [3, 6], [2, 8]]
        # sort: [[1, 4], [2, 8], [3, 6]]
        # 1) end = 0 / [1, 4]
        #    -> [1, 4] 인터벌 생성, end = 4
        # 2) end = 4 / [2, 8]
        #    -> [2, 8] 인터벌 생성, end = 8
        # 3) end = 8 / [3, 6]
        #    a) 2 <= 3임은 sort에서 이미 설정됨
        #    b) 6 < 8을 확인 했기 때문에 커버!
        intervals.sort(key=lambda x: (x[0], -x[1]))
        for _, e in intervals:
            if e > end:
                answer += 1
                end = e
        return answer
