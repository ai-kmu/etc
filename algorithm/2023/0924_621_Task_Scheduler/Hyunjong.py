class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # tasks의 개수 확인
        counts = [0] * 26
        for task in tasks:
            counts[ord(task) - ord('A')] += 1
        
        # 정렬
        counts.sort(reverse=True)
        
        # 가장 높은 task 찾기
        max_count = counts[0]
        
        # 개수 파악
        cpu = (max_count - 1) * n
        
        # 다른 task로 채우기
        for i in range(1, len(counts)):
            cpu -= min(counts[i], max_count - 1)
        cpu = max(0, cpu)
        
        # 필요한 총 시간은 태스크 수와 cpu 수의 합
        return len(tasks) + cpu
