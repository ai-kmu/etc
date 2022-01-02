class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        
        # edge case
        if n1 + n2 != n3:
            return False
        elif n1 == 0 and n2 == 0 and n3 == 0:
            return True
        
        @lru_cache(maxsize=None)
        # 재귀로 체크
        def check(s1_idx, s2_idx):
            # s1_idx나 s2_idx가 범위를 벗어날 때를 체크
            if s1_idx == n1 and s2_idx == n2:
                return True
            elif s1_idx >= n1:
                return s3[s1_idx+s2_idx] == s2[s2_idx] and check(s1_idx, s2_idx+1)
            elif s2_idx >= n2:
                return s3[s1_idx+s2_idx] == s1[s1_idx] and check(s1_idx+1, s2_idx)
            elif s1_idx + s2_idx >= n3:
                return False

            # s1_idx와 s2_idx의 character가 같을 경우를 처리
            if s3[s1_idx+s2_idx] == s1[s1_idx] and s3[s1_idx+s2_idx] == s2[s2_idx]:
                return check(s1_idx+1, s2_idx) or check(s1_idx, s2_idx+1)
            # s1과 일치할 때, 다음 위치로 가서 확인
            elif s1_idx < n1 and s3[s1_idx+s2_idx] == s1[s1_idx]:
                return check(s1_idx+1, s2_idx)
            # s2와 일치할 때, 다음 위치로 가서 확인
            elif s2_idx < n2 and s3[s1_idx+s2_idx] == s2[s2_idx]:
                return check(s1_idx, s2_idx+1)
            else: return False # 둘 다 일치하지 않을 때, false
            
        return check(0, 0)
