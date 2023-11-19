class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:

        # 모든 계산할 필요없이, tasks들을 4개로 쪼개어 각 chunck를 만들면
        # 각 chunk에서 가장 오래 걸리는 작업의 시간을 보면 됨
        # 이때, 가장 빨리 활성화되는 프로세서에 가장 오래걸리는 걸 배치해야
        # 최소시간을 달성할 수 있음
        # tasks와 processorTime을 정렬한뒤, 4개씩 했을 때 오래걸리는 조합을 찾으면 됨

        tasks = sorted(tasks)
        processorTime = sorted(processorTime, reverse=True)

        answer = 0

        for i in range(len(processorTime)):
            answer = max(answer, processorTime[i] + tasks[i * 4 + 3])

        return answer
