class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # 해당 인덱스(interval_temp)가 다른 인덱스와 좌항, 우항 하나씩 비교
        # 비교했을 때 좌항이 더 크고, 우항이 더 작거나, 반대가 확인되면 따로 저장
        # 최종적으로 두 리스트 뻄
        # 단, 메모리를 위해, deque을 통해 비교한 리스트는 제거
        from collections import deque

        # 제공된 intervals - 조건에 부합하는 리스트를 빼는 걸 목표로
        interval_ans = intervals
        # sort를 해야 순차적으로 제거 가능
        intervals = deque(sorted(intervals))
        interval_temp = []

        ans_list = []
        while intervals:
            # 현재 비교할 리스트
            interval_temp.append(intervals.popleft())
            # 조건에 부합하는 리스트 찾는 반복문
            for ri, li in intervals:
                if interval_temp[0][0] < ri and interval_temp[0][1] > li:
                    ans_list.append([ri, li])
                elif interval_temp[0][0] == ri and interval_temp[0][1] > li:
                    ans_list.append([ri, li])
                elif interval_temp[0][0] < ri and interval_temp[0][1] == li:
                    ans_list.append([ri, li])
                elif interval_temp[0][0] > ri and interval_temp[0][1] < li:
                    ans_list.append(interval_temp[0])
                elif interval_temp[0][0] == ri and interval_temp[0][1] < li:
                    ans_list.append(interval_temp[0])                
                elif interval_temp[0][0] > ri and interval_temp[0][1] == li:
                    ans_list.append(interval_temp[0])

            interval_temp = []
        
        # interval_ans에 중복되는 ans_list의 값을 제거 후 반환
        return len([x for x in interval_ans if x not in ans_list])
