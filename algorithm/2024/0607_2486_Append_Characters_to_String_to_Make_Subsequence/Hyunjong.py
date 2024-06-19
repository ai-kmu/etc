class Solution(object):
    def appendCharacters(self, s, t):
        # 초기화
        t_index = 0

        # s와 t의 문자가 같으면 전체 t 개수에서 1개씩 빼기 

        # s 문자열 순회
        for char in s:
            # t와 일치 확인
            if t_index < len(t) and char == t[t_index]:
                # 일치하는 경우 다음 t 문자와 비교
                t_index += 1

        # 남은 문자 개수 반환
        return len(t) - t_index
