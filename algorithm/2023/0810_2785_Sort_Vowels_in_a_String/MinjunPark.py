class Solution:
    def sortVowels(self, s: str) -> str:
        vs = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])  # 모음 집합
        vl = []  # 찾은 모음
        indices = []  # 모음의 위치

        s = list(s)

        for idx, letter in enumerate(s):
            if letter in vs:  # letter가 모음일 경우
                indices.append(idx)  # 그 위치를 저장
                vl.append(letter)  # letter를 저장

        vl.sort(key=lambda x: -ord(x))  # 뒤쪽 index부터 뺄 것이기 때문에 내림차순 정렬
        
        for idx in indices:  # 미리 찾아놓은 모음 위치에서 ASCII값이 작은 순으로 교체
            s[idx] = vl.pop()

        return ''.join(s)
