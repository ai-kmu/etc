class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        len_s, len_t = len(s), len(t)        
        # s와 t의 인덱스 초기화
        i, j = 0, 0
        
        # s와 t를 순회하면서 문자 있는지 확인 
        while i < len_s and j < len_t:
            # t의 현재 문자가 s에서 발견되면 t의 다음 문자로 이동
            if s[i] == t[j]:
                j += 1
            # s의 다음 문자로 이동
            i += 1  
        
        return len_t - j
