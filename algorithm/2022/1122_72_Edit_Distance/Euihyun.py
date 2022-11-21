class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp로 풀어보려고 했으나 진짜 모르겠음... 
        # 정답보고 공부하고 업데이트 했습니다.
        
        # m,n 구해놓고 dp 테이블 생성할때 null 값용 패딩
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for i in range(m+1)]
        
        # 첫번째 행과 열 업데이트 시켜줌
        for i in range(1, m+1):
            dp[i][0] = i
        for j in range(1, n+1):
            dp[0][j] = j

        # 두번째 행과 열 뒤에를 업데이트 해줌
        # 타겟 단어로 갈때 단어를 추가할지(insert), 제거할지(remove), 교체할지(replace) 중에서 골라야됨
        # 항상 최소로 업데이트 하는것이 목표
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 만약 비교하려는 문자가 같으면 replace 연산을 하게 되고
                # 연산을 할때 둘의 단어가 같기 때문에 대각선에 해당되는 replace 값을 그대로 가져옴
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                
                # 같지 않은경우는 insert, remove, replace 중에 최소값 꺼내서 + 1
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        # 타겟값과 같아 졌으니 정답 리턴
        return dp[-1][-1]
