class Solution(object):
    def numDistinct(self, s, t):
## 목적은 하위 집합을 찾는 것이다.
## 아이디어는 모든 s와 t를 순회하면서 문자열이 같을 때 이전 조합 결과 수 + 현재 끝 문제를 제외한 결과 수를 더해주면 된다.
## 끝 문자를 제외할 수 있는 이유는 무조건 맨 마지막 문자가 나와야 하기 때문이다.
        
        dp = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
        ## 각각 하위집합을 동적으로 계산하기 위한 metrix 생성 
        for j in range(len(s) + 1):
            dp[j][0] = 1
        ## 첫번째 열을 1로 채운다
        ## 왜냐하면 ''은 s의 모든 하위집합이기 때문이다.
        
        for i in range(1, len(s) + 1):## 모든 s를 순회한다.
            for j in range(1, min(i + 1, len(t) + 1)):## 모든 t를 순회한다. 이때 s가 순회된 쪽 혹은 t의 범위 끝까지만 t를 순회한다.
                                                    
                if s[i - 1] == t[j - 1]: ## 만약 두 문자열이 같으면
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1] ## 이전 결과값과 끝 문자를 제외한 결과값을 더한 값이 이번 결과값이다.
                else:
                    dp[i][j] = dp[i - 1][j] ## 두 문자열이 같지 않으면 이전 결과값만 넘겨준다.
        return dp[len(s)][len(t)]  
