class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:                       
        def merge_overlap(a, b):                                                          # 두 리스트를 병합하는 함수
            if a[1] < b[0] or b[1] < a[0]:                                                # 두 리스트가 겹치지 않는 조건
                return [a, b], False                                                      # 그대로 반환
            else:                                                                         # 겹치는 경우
                return [min(a[0], a[1], b[0], b[1]), max(a[0], a[1], b[0], b[1])], True   # [4가지 수 중 가장 작은 수, 4가지 수 중 가장 큰 수] 반환
        
        answer = []                                                                       
        intervals = sorted(intervals)                                                     # 리스트 안의 리스트들을 0번째 숫자로 정렬
        intervals = deque(intervals)                                                      # deque로 바꾸기
        while len(intervals) != 1 and intervals:                                          # 남은게 1개 또는 없는 경우 while문 종료
            a = intervals.popleft()                                                       # 첫 번째 리스트
            b = intervals.popleft()                                                       # 두 번째 리스트
            merged, if_merged = merge_overlap(a, b)                                       # 함수의 input으로 넣기
            if if_merged:                                                                 # 병합이 되었다면
                intervals.appendleft(merged)                                              # 병합된 리스트를 intervals에 삽입
            else:                                                                         # 병합이 안되었다면
                answer.append(merged[0])                                                  # 첫 번째 리스트는 answer에 넣기
                intervals.appendleft(merged[1])                                           # 두 번째 리스트는 intervals에 넣기
        if len(intervals) == 1:                                                           # while 종료 후, intervals에 남은 리스트가 있는 경우
            answer.append(intervals.pop())                                                # answer에 넣기
        return answer
