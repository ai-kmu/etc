from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        queue = deque([('0000', 0)])
        deadends = set(deadends)

        while queue:
            # bfs로 풀이
            num, count = queue.popleft()
            if num == target:
                return count
            
            for i in range(4):
                for diff in [-1, 1]:
                    new_num = num[:i] + str((int(num[i]) + diff) % 10)
                    if i < 3:
                        new_num += num[i+1:]
                    if new_num not in deadends:
                        queue.append((new_num, count + 1))
                        # visit 처리
                        deadends.add(new_num)
        
        return -1
