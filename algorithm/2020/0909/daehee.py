class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:                     # 간격 없는 경우 바로 리턴
            return []
        
        intervals.sort()
        answer = [intervals[0]]                     # 첫번째 간격 넣고 시작
        
        for itv in intervals[1:]:                   
            if answer[-1][1] >= itv[0]:             # 현재 간격과 대상 간격이 겹치는 경우
                if answer[-1][1] > itv[1]:          # 현재 간격이 대상 간격에 포함되는 경우
                    continue
                answer[-1] = [answer[-1][0],itv[1]] # 현재 최소 범위와 대상 최대 범위 합집합
                continue
            answer.append(itv)
                
        return answer
