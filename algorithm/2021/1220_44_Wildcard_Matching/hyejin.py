class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # s와 p가 빈 string이면 True
        # p가 빈 스트링이면 False 
        if not s and not p:
            return True
        elif not p:
            return False
        
        # 결과 cache
        @functools.lru_cache(None)
        def dp(i, j):
            # p가 끝까지 갔고, *이면 match 성공
            if j == len(p) and p[-1] == '*':
                return True
            elif j == len(p): # 끝까지 갔으면, i도 같이 끝까지 가야함.
                return i == len(s)
            
            # s[i]와 p[j]가 일치하는지 체크
            match = i < len(s) and (s[i] == p[j] or '?' == p[j])
            
            
            if match: # 일치하면 다음 위치
                return dp(i + 1, j + 1)
            elif p[j] == '*': # p[j]가 *면 
                while j + 1 < len(p) and p[j + 1] == '*':
                    j += 1
                # s의 위치를 i+1로 이동하거나, j+1도 *라면 j+1로 이동해서 가능한지 체크 (끝이 *일 경우)
                return (i + 1 < len(s) and dp(i + 1, j)) or dp(i, j + 1)
            

        # dynamic progrmming 0번째부터 시작
        return dp(0, 0)
