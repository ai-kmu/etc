# 투 포인터로 풀이
class Solution:
    def areSentencesSimilar(self, sentence1, sentence2):
        # 단어로 쪼갬
        s1, s2 = sentence1.split(), sentence2.split()

        # 긴 쪽을 s1으로 설정
        if len(s1) < len(s2):
            s1, s2 = s2, s1

        i, j, diff = 0, len(s2)-1, len(s1)-len(s2)

        # 포인터를 움직여가며 유사도 파악
        while i < len(ans2) and s1[i] == s2[i]:
            i += 1 

        while j >= 0 and s2[j] == s1[j+diff]:
            j -= 1

        return i > j
