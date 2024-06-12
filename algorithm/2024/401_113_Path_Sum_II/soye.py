class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0  # 문자열 s의 인덱스를 나타내는 변수
        j = 0  # 문자열 t의 인덱스를 나타내는 변수
        while i < len(s) and j < len(t):  # s와 t의 끝에 도달할 때까지 반복
            if s[i] == t[j]:  # s와 t의 현재 문자가 같으면
                i += 1  # s의 인덱스를 하나 증가
                j += 1  # t의 인덱스를 하나 증가
            else:
                i += 1  # s의 인덱스만 하나 증가 (t의 현재 문자는 유지)
        return len(t) - j  # t에서 매칭되지 않은 남은 문자 수 반환
