class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 1. 문제 파악
        # target까지 자물쇠를 돌리는데,
        # deadends를 피해서 최적의 횟수로 도달해야함

        # 2. 알고리즘 설계
        # BFS로 구현

        def up(s):
            return '0' if int(s) == 9 else str(int(s) + 1)

        def down(s):
            return '9' if int(s) == 0 else str(int(s) - 1)

        to_visit = deque()
        visited = set()

        for i in deadends:
            visited.add(i)
        
        flag = -1

        to_visit.append(('0000', 0))

        while to_visit:
            cur, d = to_visit.popleft()        
            if cur in visited:
                continue

            visited.add(cur)

            if cur == target:
                flag = d
                break

            if cur != target:
                temp = list(cur)
                for i in range(4): # BFS
                    a = ''.join(temp[:i]) + up(temp[i]) + ''.join(temp[i+1:])
                    b = ''.join(temp[:i]) + down(temp[i]) + ''.join(temp[i+1:])
                    if a not in visited:
                        to_visit.append((a, d + 1))
                    if b not in visited:
                        to_visit.append((b, d + 1))

        return flag  
