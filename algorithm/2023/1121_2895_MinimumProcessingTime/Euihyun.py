class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        '''
        ProcessorTime 이 작을때 task 큰걸 처리하고
        ProcessorTime 이 클때 task 작은걸 처리하면 최소시간 가능
        '''
        # ProcessorTime 은 작은거 부터
        processorTime.sort()
        # Task는 큰거부터
        tasks.sort(reverse=True)
        n = len(processorTime)
        
        temp = []
        # ProcessorTime 바로
        if n == 1:
            return processorTime[0] + tasks[0]
        # ProcessorTime 여러개면 해당 ProcessorTime에 가장큰값 더해서 temp에 추가
        for i in range(n):
            temp.append(processorTime[i]+tasks[i*4])

        return max(temp)
