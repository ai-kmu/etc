class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

            # 시작 순으로 정렬
            # 하나씩 보면서 이전의 오른쪽이 현재의 오른쪽보다 큰것이 있는지 확인
            l_point_sort = sorted(intervals, key = lambda x : (x[0], -x[1]))
            prev_max_r = 0
            answer = len(intervals)

            for l, r in l_point_sort:
                if prev_max_r >= r:
                    answer -= 1
                prev_max_r = max(r, prev_max_r)
            
            return answer
