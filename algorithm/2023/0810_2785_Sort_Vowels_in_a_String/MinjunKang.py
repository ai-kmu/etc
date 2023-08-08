class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        # 모음 인덱스, 값 추출
        indices = []
        v = []
        for i, _ in enumerate(s):
            if _.lower() in vowels:
                indices.append(i)
                v.append(_)
        # 정렬
        v.sort()
        # 기존 s에 정렬된 모음 값으로 대치를 위해 charactor 단위로 분리
        ans = [*s]
        # 순서에 따라 모음 대치
        if indices:
            for i, k in enumerate(v):
                ans[indices[i]] = k
        return ''.join(ans)
