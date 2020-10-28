class Solution:
    def magicalString(self, n: int) -> int:
        idx = 2
        S = [1, 2, 2]                 # 초기 스트링
        while n >= len(S):            # n개까지 추가하기
            last = S[-1]              # 추가할 숫자 구하기 위한 마지막 숫자 (반대 숫자 추가)
            for _ in range(S[idx]):   # S[idx] 만큼 붙여줌
                S.append(3-last)
            idx += 1
        answer = S[:n].count(1)       # 1 
        return answer
