'''
DP로 푼 건데
memoization을 위한 array 따로 지정하지 않고
triangle을 업데이트 해서 memoization 했습니다.
될까 싶어서 했는데 오히려 더 빠르고 메모리도 적게 들더라구요.
'''

class Solution:
    def minimumTotal(self, triangle):
        depth = len(triangle)       # 주어진 삼각형 행의 개수

        # 1. 예외처리: depth = 1이면 요소 하나 들어옴. 그대로 return
        if depth == 1:
            return triangle[0][0]

          
        # 2. 업데이트: 그래서 row = 1부터 진행
        for row in range(1, depth):
            # 맨 왼쪽: 왼쪽끼리 더함
            triangle[row][0] = triangle[row-1][0] + triangle[row][0]

            # 중간: 위의 왼쪽 (row-1, i-1)랑 오른쪽 (row-1, i)을 비교해서
            #       작은 거에 (row, i)를 더함. (큰 쪽은 답이 될 가능성 x)
            for i in range(1,row):
                triangle[row][i] = min(triangle[row-1][i-1], triangle[row-1][i]) + triangle[row][i]
            
            # 맨 오른쪽: 오른쪽끼리 더함
            triangle[row][row] = triangle[row-1][row-1] + triangle[row][row]

            
        # 3. 답: 업데이트가 끝난 뒤, 마지막 행에서 최솟값 반환
        return min(triangle[-1])
