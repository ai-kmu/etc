from collections import Counter

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        l = len(tasks)

        if n == 0: # cooldown이 필요없다면 그냥 길이 리턴
            return l

        cnt = Counter(tasks)
        max_cnt = 0
        max_val = max(cnt.values())

        for key, val in cnt.items():
            if val == max_val:
                max_cnt += 1
        return max((n + 1) * (max_val - 1) + max_cnt , l)
