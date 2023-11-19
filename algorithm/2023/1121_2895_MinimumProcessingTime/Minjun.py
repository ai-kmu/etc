'''
각 프로세서는 한 번의 일(4 task)만 수행할 수 있으므로
단순 그리디
'''

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        time = 0
        cnt = 0
        # 제일 실행시간 빠른 프로세서부터 4개씩 긴 task 할당
        for i, pt in enumerate(processorTime):
            for t in tasks[i*4:]:
                if time < pt+t:
                    time = pt+t
                cnt +=1
                if cnt == 4:
                    cnt = 0
                    break

        return time
