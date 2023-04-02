from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # bfs를 활용한 풀이
        queue = deque([("0000", 0)])
        # 효율성을 높이기 위해 deadends를 set으로 바꿈
        deadends = set(deadends)
        visited = set(["0000"])
        
        while queue:
            num, count = queue.popleft()
            
            if num in deadends:
                continue
            elif num == target:
                return count
            
            # 실제 자물쇠를 돌리듯, 각 자리수를 한칸 올리거나 내린다
            for i in range(4):
                tmp = int(num[i])
                new_num = num[:i] + str((tmp + 1) % 10) + num[i+1:]
                if new_num not in visited:
                    visited.add(new_num)
                    queue.append((new_num, count+1))
                new_num = num[:i] + str((tmp - 1) % 10) + num[i+1:]
                if new_num not in visited:
                    visited.add(new_num)
                    queue.append((new_num, count+1))
        
        return -1
        
