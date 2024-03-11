class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0], -x[1])) # 시간 순, 구간 길이가 긴 순으로 정렬
        
        ret = [intervals[0]] # 처음 구간 default
        
        for i in range(1, len(intervals)): # 추가된 구간의 끝(ret[-1][1])과 intervals 안의 i번째 구간의 끝(intervals[i][1])을 비교
            if ret[-1][1] >= intervals[i][1]: # 마지막으로 추가된 구간의 끝(ret[-1][1])이 더 크다면 intervals[i]는 ret[-1]에 포함되므로 continue
                continue

            ret.append(intervals[i]) # 그렇지 않을 경우 포함 관계가 아니기 때문에 ret list에 추가
            
        
        return len(ret) # 최종 길이 반환
        