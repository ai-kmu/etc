# 답 봤어요 리뷰 안해주셔도 됩니다.
from collections import Counter 

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 작업 빈도를 세는 Counter 객체 생성
        task_counts = Counter(tasks)
        
        # 가장 많이 나온 작업의 빈도를 찾음
        max_frequency = max(task_counts.values())
        
        # 가장 많이 나온 작업의 수(count) 초기화
        count = 0
        
        # 모든 작업 중에서 가장 많이 나온 작업의 수(count)를 찾음
        for val in task_counts.values():
            if val == max_frequency:
                count += 1
        
        # 최소 시간 계산 및 반환
        # 최소 시간 = (가장 많이 나온 작업의 빈도 - 1) * (쿨다운 간격 n) + 가장 많이 나온 작업의 수(count) - 1
        # 또는 최소 시간 = 작업의 총 개수(len(tasks))
        return max(max_frequency + (max_frequency - 1) * n + count - 1, len(tasks))
