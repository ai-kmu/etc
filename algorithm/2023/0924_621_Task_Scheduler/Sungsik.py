from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = [(-v, k) for k, v in Counter(tasks).items()]
        cooldown = deque([])
        task_heap = []
        
        for task in tasks:
            heapq.heappush(task_heap, task)
        
        count = 0
        
        while task_heap or cooldown:
            # task가 남아있으면 이를 수행하고 cooldown에 추가
            if task_heap:
                v, k = heapq.heappop(task_heap)
                if v < -1:
                    cooldown.append((count, v+1, k))
            
            # cooldown이 있고 n만큼 쉬었다면 이를 heap에 추가
            if cooldown and count - cooldown[0][0] >= n:
                _, v, k = cooldown.popleft()
                heapq.heappush(task_heap, (v, k))
                        
            count += 1
            
        return count
