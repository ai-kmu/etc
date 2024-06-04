class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ret = 0
        start_idx = 0
        
        for i in s:  # s 문장 탐색
            if start_idx >= len(t):  # t 문장 길이 도달 시 종료
                break

            elif i == t[start_idx]:  # s 문장 탐색 시 t의 start_idx 위치의 문자 일치 시 start_idx 증가
                start_idx += 1

        return len(t) - start_idx  # t의 남은 문장 길이 반환
        
