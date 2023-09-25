from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # trivial case
        if n == 0:
            return len(tasks)
        a = defaultdict(int)
        for _ in tasks:
            a[_] += 1
        b = sorted(a.values(), reverse=True)
        start = 0
        visit = []
        for _ in b:
            for i in range(_):                
                if i == 0 :
                    now = start
                else:
                    now = prev + (1 + n)
                if now in visit:
                    while now not in visit:
                        now += 1                    
                        prev = now
                prev = now
                visit.append(now)
                    
            start += 1
        print(visit)
        return max(visit)+1
