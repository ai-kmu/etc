from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        queue = deque()
        total_n = len(s)
        for sub_str in wordDict:
            n = len(sub_str)
            if n <= total_n and s[:n] == sub_str:
                queue.append((sub_str, n))
        
        answer = []
        
        while queue:
            prev_str, prev_n = queue.popleft()
            if prev_n == total_n:
                answer.append(prev_str)
                continue
            
            for sub_str in wordDict:
                n = len(sub_str)
                if prev_n + n <= total_n and s[prev_n:prev_n+n] == sub_str:
                    queue.append((prev_str + " " + sub_str, prev_n + n))
        
        return answer
