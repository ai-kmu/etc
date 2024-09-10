class Solution:
    def areSentencesSimilar(self, st1: str, st2: str) -> bool:
        # word 리스트로 변경
        st1 = st1.split(" ")
        st2 = st2.split(" ")

        len1 = len(st1)
        len2 = len(st2)
        
        # 짧은 걸 1로 설정
        if len1 > len2:
            st1, st2 = st2[:], st1[:]
            len1, len2 = len2, len1
        elif len1 == len2:
            return st1 == st2
        
        # 왼쪽 오른쪽 순서대로 탐색하면서 얼마나 겹치는지 확인함
        i = 0
        # 왼쪽부터 탐색
        while i < len1 and st1[i] == st2[i]:
            i += 1
        # 오른쪽부터 탐색 - 왼쪽에서 겹쳤던 건 제외!
        while i < len1 and st1[i] == st2[len2 - len1 + i]:
            i += 1

        # 모두 겹쳤다면 끗
        return i == len1
