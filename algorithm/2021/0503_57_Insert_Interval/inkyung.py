class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = list()
        if intervals is None:
            return answer.append(newInterval)
        
        for interval in intervals:
            # 겹치는 경우가 없고 newInterval 값이 현재 값보다 큰 경우
            if interval[1] < newInterval[0]:
                answer.append(interval)
            # 겹치는 경우가 없고 현재 interval 값이 newInterval보다 큰 경우
            elif interval[0] > newInterval[1]:
                answer.append(newInterval)
                newInterval = interval
            # 겹치는 경우가 발생해서 최대값과 최소값을 결정해서 새로운 값 결정
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
                
        answer.append(newInterval)
        return answer
