# levinshtien distance(edit distance) 알고리즘
# 문자열의 유사도를 계산할 때 사용된다고 함.
# word1을 insert, delete, replace를 최소한으로 사용하여 word2로 변경하는 방법
# Dynamics Programming(DP) 사용

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # word1이나 word2가 빈 스트링일 경우
        if len(word1) == 0 or len(word2) == 0:
            return abs(len(word2)- len(word1))
        
        # distance를 저장할 matrix (m+1) x (n+1) 초기화
        lev_dist = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        # 초기값 설정해주기
        for i in range(len(word1)+1): # 밑으로 움직이는 건 delete
            lev_dist[i][0] = i
        
        for j in range(len(word2)+1): # 오른쪽으로 움직이는 건 insert
            lev_dist[0][j] = j
            
        # word1, word2의 첫글자부터 비교 시작
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]: # 같으면 (i-1, j-1)의 distance를 그대로 가져올 수 있음.
                    lev_dist[i][j] = lev_dist[i-1][j-1]
                else: # 아니면 (왼쪽, 위, 대각선 위)의 distance에 +1을 하여 min을 구함
                    lev_dist[i][j] = min(lev_dist[i-1][j-1]+1, lev_dist[i][j-1]+1, lev_dist[i-1][j]+1)
        

        return lev_dist[-1][-1]
