from collections import defaultdict

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        late_run = defaultdict(int)
        days = 1

        # 각 task id별로 space 고려하여 day 업데이트
        for key in tasks:
            if late_run[key]: # 값 있으면 현재 일자와 space 고려한 일수 비교
                late_run[key] = max(days, late_run[key] + space + 1)

            else: # 초기 정의
                late_run[key] = days

            days = late_run[key] + 1 # day 업데이트
            

        return late_run[tasks[-1]]
