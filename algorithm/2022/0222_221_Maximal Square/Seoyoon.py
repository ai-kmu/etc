#주어진 배열에서 값이 모두 1인 정사각형 중 가장 큰 정사각형을 찾는 문제

# Maximal Rectangle 문제와 유사하게 풀이

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        #결과를 저장할 변수 answer 
        answer = 0 
        
        # dp array 생성
        dp = [0] * (len(matrix[0])+1)
        
        # 행을 위에서 아래로 보면서 현재 행까지 연속 1인 수를 추적한다. 
        for row in matrix:
            for i in range(len(row)):
                if row[i] == '1':
                    dp[i] += 1
                else: 
                    dp[i] = 0
            

            # 단조(증가 스택)을 사용해서 히스토그램의 각 열을 보고 높이가 증가하면 계속 stack
            #그렇지 않은 경우 스택의 맨 위가 현재 높이보다 낮아질 때까지 pop 하고 다음 스텍을 계속한다.
            # 여기서 우리는 index를 스택에 저장한다.
            stack = [-1]
            for i in range(len(dp)):
                while stack and dp[stack[-1]] > dp[i]:
                    j = stack.pop()
                    
                    #스택에서 나올 때마다 최대 제곱의 면적을 계산하고 업데이트
                    area = min((i - stack[-1] - 1), dp[j]) ** 2
                    answer = max(answer, area)
                stack.append(i)
        
        return answer
