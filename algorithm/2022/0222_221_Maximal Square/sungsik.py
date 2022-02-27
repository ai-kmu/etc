class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp를 활용한 풀이
        # base case: 0번째 행과 열에서 1일 경우 모서리의 길이가 1인 정사각형
        # recursive equation:
        #   현재 위치에서 0일 경우 
        #   - 그것을 포함하는 정사각형은 없으므로 0
        #   현재 위치에서 1일 경우
        #   - 위쪽과 왼쪽 정사각형의 크기를 가져온 후
        #       - 둘의 크기가 다를 경우 둘 중 다른 것에서 1을 더한다.
        #       - 둘의 크기가 같을 경우 왼쪽 위 꼭지점이 1인지 확인해야 한다.
        #           - 위,왼쪽 정사각형의 크기가 위와 왼쪽 정사각형보다 크거나 같을 경우 꼭짓점이 1이다.
        #           - 꼭짓점이 1일 경우 해당 사각형의 크기를 그대로 사용하고 아닐 경우 1을 뺀다.
        #           - 마찬가지로 1을 더한다.
        # 이렇게 해서 모든 위치에서 값을 다 구하고 최댓값을 출력한다.
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        
        # base case
        # 0번째 행
        for i in range(m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
        # 0번째 열
        for i in range(n):
            if matrix[0][i] == '1':
                dp[0][i] = 1
        
        # recursive equation
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    edge = 0
                    
                    # 위, 왼쪽 정사각형의 크기를 가져옴
                    up = dp[i-1][j]
                    left = dp[i][j-1]
                    
                    # 앞서 언급한 case에 따라 edge를 구함
                    if up == left:
                        edge = up if dp[i-1][j-1] >= up else up-1
                    else:
                        edge = min(up, left)
                    dp[i][j] = edge + 1
                    
        max_edge = max([max(x) for x in dp])
        return max_edge ** 2
