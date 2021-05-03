class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 새로운 interval을 기존 intervals에 더하고 정렬
        intervals = intervals + [newInterval] 
        intervals.sort()
        
        result = [] # 문제의 답 리스트 초기화
        for i in intervals:
            if not result or (result[-1][1] < i[0]): # result가 비어있거나 누적된 result의 맨 끝값이 현재 i interval의 첫번째 값보다 작으면
                result.append(i) # 현재 interval i를 result에 추가
                
            else: # 누적된 result의 마지막 값이 현재 i interval의 첫번째 값보다 크면
                result[-1][1] = max(i[1], result[-1][1]) # 현재 i interval의 두번째 값과 누적된 result의 맨 끝값 중 큰것을 현재 result의 맨 끝값으로 설정
                
        return result
