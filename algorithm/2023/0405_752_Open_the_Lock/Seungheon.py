from collections import deque 

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # seen == 방문한곳 == 가면 안되는곳
        seen = set(deadends)
        # 예외처리
        if '0000' in seen:
            return -1
        min_count = float('inf')
        # (시작값, 이동횟수)
        nums = deque([('0000',0)])
    
        # BFS탐색
        while nums:
            num, count = nums.popleft()
            
            # 발견하면 return
            if target == num:
                min_count = min(min_count, count)
                return min_count
            
            # 각 자리에서 1을 더하거나 1을 빼서 탐색
            for i, n in enumerate(num):
                for sign in [-1,1]:
                    tmp = list(num)
                    tmp[i] = str((int(tmp[i]) + 10 + sign)%10)
                    tmp_num = ''.join(tmp)
                    if tmp_num in seen:
                        continue
                    seen.add(tmp_num)
                    nums.append((tmp_num, count+1))
        
        # 발견하지 못했으면 -1
        return -1
