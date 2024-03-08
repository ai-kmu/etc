# 나도 1솔?
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        tot = 0
        prev_s, prev_e = 0, 0 
        intervals.sort()
        for _ in intervals:
            s, e = _
            # 현재 시작(s)이 이전 마지막(prev_e)보다 크면 안 겹침. -> +=1 하고 기준 초기화
            if s >= prev_e:
                prev_s = s
                prev_e = e
                tot += 1
            # 겹치는 부분이 있다.
            else:  # s <<< prev_e.   ->.  e > prev_e.  or. e  < prev_e
                # 현재 끝이 이전 마지막보다 크면,  (작으면 고려할 필요조차 없음 ㅡㅡ)
                if e > prev_e:
                    # 스타트가 같은 상태면, 마지막 포인트만 끌어댕겨줌
                    if s == prev_s:
                        prev_e = e
                        continue
                    # 스타트가 다르면, 다른 녀석이기 때문에 +=1 하고 기준 초기화
                    tot += 1
                    prev_s = s
                    prev_e = e
        return tot                    
