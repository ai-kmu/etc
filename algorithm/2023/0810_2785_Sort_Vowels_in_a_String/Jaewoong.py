class Solution:
    def sortVowels(self, s: str) -> str:
        vow = []
        pos = []
        
        # vowel 만 먼저 찾고, vowel 끼리 sort 함
        # 이때 index도 같이 저장
        for i, ch in enumerate(s):
            if ch.lower() in {'a', 'e', 'i', 'o', 'u'}:
                vow.append(ch)
                pos.append(i)
        
        vow.sort()
        # s를 list로 바꾸고, list값을 인덱스를 기준으로 값을 변경한다.
        answer = list(s)
        for i,v in zip(pos, vow):
            answer[i] = v
        
        return ''.join(answer)
