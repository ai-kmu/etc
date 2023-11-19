class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        # 시간이 긴 task 부터 처리하기 위함
        # 4개씩 슬라이싱 프로세스 할당

        tasks.sort(reverse = True)
        processorTime.sort()
            
        return max([pt + max(tasks[i * 4 : (i + 1) * 4]) for i, pt in enumerate(processorTime)])
