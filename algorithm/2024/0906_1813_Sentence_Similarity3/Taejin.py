class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # sentence1이 sentence2보다 항상 길이가 긴 문장이 되도록 설정
        if len(sentence1) < len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        
        # 탐색 인덱스 선언 및 sentence split
        s1 = sentence1.split()
        s2 = sentence2.split()
        start_idx = 0
        end_idx = -1

        # 시작과 끝 인덱스부터 공통되지 않은 부분의 인덱스 탐색
        for _ in range(len(s2)):
            if s1[start_idx] == s2[start_idx]:
                start_idx += 1

            if s1[end_idx] == s2[end_idx]:
                end_idx -= 1
        
        # s2를 기준으로 모두 탐색하면 len(s2)의 배수가 되므로 맞으면 True
        if (start_idx - end_idx - 1) // len(s2):
            return True

        return False
