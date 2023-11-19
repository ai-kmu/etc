class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        ans = 0
        # 가장 오래 걸리는 processorTime이 가장 수행 시간이 짧은 task를 선택하도록 sort
        processorTime.sort(reverse=True)
        tasks.sort()
        # processorTime을 순회하면서 하나의 processor가 4개의 task를 순회
        for i, v in enumerate(processorTime):
            for j in range(4):
                # 가장 오래 수행시간이 걸리는 값을 return
                ans = max(ans, v + tasks[(i * 4) + j])
        return ans
