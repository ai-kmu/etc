class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        
        # s1이 s2보다 긴 것을 가정
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        
        n = len(s2)
        
        # 앞에서 부터 같은지 비교
        i = 0
        while i < n and s1[i] == s2[i]:
            i += 1
        
        # 남은 sentence가 뒤에서 부터 같은지 비교
        return s1[i-n:] == s2[i-n:] or i == n
