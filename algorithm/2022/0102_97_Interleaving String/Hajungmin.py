class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 2차원 dp 생성
        dp = [[False] * (len(s2)+1) for _ in range(len(s1)+1)]
        # 0,0을 true로 초기화
        dp[0][0] = True
        
        #만약 s1과 s2의 길이를 더했을 때 s3의 길이가 안나오면 false를 반환
        if len(s1) + len(s2) != len(s3): return False
        
        # 먼저 dp배열의 첫번째 행과 열을 채운다
        
        for i in range(1, len(s1)+1):
            # 만약 s1과 s3의 문자가 같고 이전 dp배열의 값이 True라면 현재 dp배열 값을 True로 넣어준다.
            '''
                코드 수정 by 김성식
                한번 False가 되면 그 이후는 무조건 False가 되므로
                break문을 추가
            '''
            if s1[i-1] == s3[i-1]:
                dp[i][0] = True
            else:
                break
            
        for j in range(1, len(s2)+1):
            # 만약 s2와 s3의 문자가 같고 이전 dp배열의 값이 True라면 현재 dp배열 값을 True로 넣어준다.
            if s2[j-1] == s3[j-1]:
                dp[0][j] = True
            else:
                break
            
        # 이후 이중 for문을 돌며 s1과 s3를 비교한 뒤 이전 dp배열을 확인하여 True일시 현재 dp배열에 true를 넣는 방식으로 s2도 동일하게 조건문을 세워준다.    
        for i in range(1, len(s1)+1):
              for j in range(1, len(s2)+1):
                    dp[i][j] = (s1[i-1] == s3[i+j-1] and dp[i-1][j]) or (s2[j-1] == s3[i+j-1] and dp[i][j-1])
        # 이후 dp배열의 가장 마지막 값을 반환한다
        return dp[-1][-1]
