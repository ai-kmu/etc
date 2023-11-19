'''
processorTime이 작은 녀석이 큰 tasks를 맡아야 함
'''
class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        # tasks를 오름차순으로 정렬
        tasks_sorted = sorted(tasks)
        # processorTime을 내림차순으로 정렬 
        processorTime_sorted = sorted(processorTime, reverse=True)

        # 3, 7, 11, ... 인덱스가 각각의 processor가 처리해야 할 가장 오래걸리는 task의 시간을 의미
        idx = 3
        max_time_per_processor = []

        # 반복문을 돌면서 processor 마다 가장 오래 걸리는 시간을 리스트에 저장
        for i in processorTime_sorted:
            max_time_per_processor.append(i+tasks_sorted[idx])
            idx += 4

        # 리스트 중 최댓값이 전체의 최소 시간을 의미
        return max(max_time_per_processor)
