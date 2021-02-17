class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        path = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]        # 빈 2차원 리스트 생성하기
        for j in range(len(word2)+1):                                                 # 공백과 문자와의 거리 생성
            path[j][0] = j
        for i in range(len(word1)+1):                                                 # 공백과 문자와의 거리 생성
            path[0][i] = i
        
        for j in range(1, len(word2)+1):                                              
            for i in range(1, len(word1)+1):
                if word1[i-1] == word2[j-1]:                                           # 두 글자가 같다면
                    path[j][i] = path[j-1][i-1]                                        # 대각선에 있는 글자를 그대로 가지고 온다 ( 변경 필요 X )
                else:                                                                  # 다르다면
                    path[j][i] = min(path[j-1][i], path[j-1][i-1], path[j][i-1]) + 1   # 이전 경로에서 자르기 바꾸기 빼기 등을 사요애야 하기 때문에 이전 경로들 중 가장 작은 값에 1을 더해
        return path[len(word2)][len(word1)]                                            # 업데이트한다.
