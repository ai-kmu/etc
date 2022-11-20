"""
DP 결과

   '' h o r s e
''  0 1 2 3 4 5
 r  1 1 2 2 3 4
 o  2 2 1 2 3 4
 s  3 3 2 2 2 3
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)

        # 빈 문자열이 들어왔을 때를 대비한 패딩 포함
        DP = [[-1 for _ in range(N+1)] for _ in range(M+1)]

        # 빈 문자열과 비교하는 경우: insert 혹은 delete만 하면 됨
        for i in range(N+1):
            DP[0][i] = i
        for i in range(M+1):
            DP[i][0] = i

        # DP 시작: bottom-up
        for j in range(1, M+1):
            for i in range(1, N+1):
                # 같을 경우: 이전 알파벳을 비교함
                if word1[i-1] == word2[j-1]:
                    DP[j][i] = DP[j-1][i-1]
                # 다를 경우
                else:
                    # 삽입
                    insert = DP[j-1][i]
                    # 삭제
                    delete = DP[j][i-1]
                    # 교체
                    replace = DP[j-1][i-1]
                    # 셋 중 가장 적은 코스트를 갖고 오고 1을 더함
                    DP[j][i] = min(insert, delete, replace) + 1

        # 답은 마지막 원소
        return DP[M][N]
