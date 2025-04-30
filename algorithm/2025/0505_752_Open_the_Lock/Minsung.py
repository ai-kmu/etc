from collections import Counter, deque, defaultdict
'''
경우의 수 : 10000(0~9999) -> 애지간하면 time limied 안 걸릴 듯? -> 걸리네...
실패...
'''

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        dead = Counter(deadends)
        q = deque([['0000', 0]])
        visited = defaultdict(bool)

        while q:
            cur_wheel, cnt = q.popleft()
            visited[cur_wheel] = True
            for i in range(4):
                cur_num = int(cur_wheel[i])

                next_num = cur_num+1 if cur_num+1 != 10 else 0
                next_wheel = list(cur_wheel)
                next_wheel[i] = str(next_num)
                next_wheel = ''.join(next_wheel)
                if dead[next_wheel]!=1 and visited[next_wheel]!=True:
                    if next_wheel == target:
                        return cnt+1
                    q.append([next_wheel, cnt+1])

                next_num = cur_num-1 if cur_num-1 != -1 else 9
                next_wheel = list(cur_wheel)
                next_wheel[i] = str(next_num)
                next_wheel = ''.join(next_wheel)
                if dead[next_wheel]!=1 and visited[next_wheel]!=True:
                    if next_wheel == target:
                        return cnt+1
                    q.append([next_wheel, cnt+1])

        return -1
