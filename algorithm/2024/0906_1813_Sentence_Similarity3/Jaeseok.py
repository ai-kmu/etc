class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # 풀이 실패 solution 참고함

        # s1이 무조건 더 짧도록 하기 위함
        if len(sentence1) > len(sentence2):
            sentence1, sentence2 = sentence2, sentence1

        # 단어 단위로 잘라줌
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")

        n, i, j = len(s1), 0, 1
        # 정방향으로 가장 겹치는 부분까지 탐색
        while i < n and s1[i] == s2[i]:
            i += 1
        # 역방향으로 가장 겹치는 부분까지 탐색
        while j < n + 1 and s1[-j] == s2[-j]:
            j += 1
        
        # 겹치는 부분은 이제 가장 긴 sentence가 되므로 s1의 길이보다 길어야 similar
        return i + j > n
