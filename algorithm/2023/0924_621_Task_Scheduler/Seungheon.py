from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # 한 사이클을 n+1번으로 두고, 
        # 한사이클을 돈 후에 재정렬하여 greedy하게 개수가 많은것부터 수행

        ddict = defaultdict(int)
        for ch in tasks:
            ddict[ch] += 1
        
        # 남은 task 수
        task_len = len(tasks)
        answer = 0

        while task_len != 0:
            # 정렬
            sorted_dict = sorted(ddict.items(), key = lambda x : x[1], reverse=True)
            
            # n번 수행
            for i in range(n+1):
                # 남은 task가 있을 때 & len(task) < n 일때
                if i < len(sorted_dict) and ddict[sorted_dict[i][0]] != 0:
                    ddict[sorted_dict[i][0]] -= 1
                    answer += 1
                    task_len -= 1
                # 남은 task가 없을 때(idle)
                else:
                    if task_len == 0:
                        break
                    answer += 1

        return answer
