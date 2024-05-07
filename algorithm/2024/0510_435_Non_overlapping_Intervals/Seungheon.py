class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        answer = 0

        intervals.sort(key = lambda x : (x[0], x[1]))

        # initialization
        tmp_s = intervals[0][0] # 마지막으로 사용하는것의 왼쪽
        tmp_e = intervals[0][1] # 마지막으로 사용하는것의 오른쪽

        # 해당 경우마다 처리
        for s, e in intervals[1:]:
            # ----
            #       -----
            if s >= tmp_e:
                tmp_s = s
                tmp_e = e
            # ----------
            #    -----
            elif s >= tmp_s and e <= tmp_e:
                tmp_s = s
                tmp_e = e
                answer += 1
            # ----
            #    -----
            else:
                answer += 1
 
        return answer
