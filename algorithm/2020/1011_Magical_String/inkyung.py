import collections
class Solution:
    def magicalString(self, n: int) -> int:
        """
        규칙:
        마지막 값이 1인지 2인지에 따라서 i값을 늘려가면서 S[i]에 있는 값만큼 1이나 2를 추가해줌
        """
        S = [1, 2, 2]
        i = 2
        while len(S) < n:
            last_val = 2 if S[-1] == 1 else 1 # 지금까지 저장된 마지막 값이 무엇인지를 판단
            S.extend([last_val] * S[i])   # S에 마지막 값을 S[i]개만큼 추가해줌
            i += 1
        return S[:n].count(1)
