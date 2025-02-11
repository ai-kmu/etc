class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # 가능한 최댓값인 avail부터 repeated word를 생성, 가능한지 파악하는 전략
        m = len(sequence)
        n = len(word)
        avail = m // n  # 가능한 최댓값

        # 반대로 탐색해서 최대한 빠르게
        for k in range(avail, 0, -1):
            repeat = word * k  # i번 반복한 repeated word 생성
            if repeat in sequence:
                return k  # 되면 그게 끝
        
        return 0  # for문 다 돌면 불가능한 거니까 0
