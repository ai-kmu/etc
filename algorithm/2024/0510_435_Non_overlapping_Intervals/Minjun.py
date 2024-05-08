class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 정렬
        intervals.sort()
        # 비교 기준점(끝 점)
        p = intervals[0][-1]
        cnt = 0
        for s, e in intervals[1:]:
            # 기준점보다 시작점이 크면 삭제 못 함, 기준점 교체
            if s >= p:
                p = e                
                continue
            # 시작점이 작으면 삭제 가능
            else:
                # 끝점조차 작으면(포함관계), 이전 기준점을 날림(더 큰 걸 날리는게 유리)
                if e <= p:
                    cnt += 1
                    p = e
                # 애매하게 겹치면 기준점 유지
                else:
                    cnt += 1
        return cnt

