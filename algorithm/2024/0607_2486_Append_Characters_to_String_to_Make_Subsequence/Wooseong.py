class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # 특수 케이스: 이미 s가 t를 포함함
        if t in s:
            return 0
        
        # s, t를 앞부터 탐색하면서
        i = j = 0
        while (i < len(s)) and (j < len(t)):
            if s[i] == t[j]:
                j += 1  # 같은 거 발견하면 t는 한 칸 옮겨도 됨
            i += 1  # s는 아무튼 계속 옮기면서 탐색
        
        # t의 길이에서 같은 거 (j)의 개수 뺀 게 답
        return len(t) - j
