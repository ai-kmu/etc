# Time Limit Exceeded
# test case는 통과
class Solution(object):
    
    def minimumTotal(self, triangle):
        # 예외 처리
        if len(triangle) == 1:
            return triangle[0][0]
        # 0, 0 시작
        return self.recursive(triangle, 0, 0)
    
    # i : 세로, j 가로
    def recursive(self, triangle, i, j):
       
        # 다음 층이 마지막 층인 경우 return 
        if i + 2 == len(triangle):
            return triangle[i][j] + min(triangle[i+1][j], triangle[i+1][j+1])
        
        # 아직 층이 남아 있는 경우 재귀함수 호출
        return triangle[i][j] + min(self.recursive(triangle, i+1, j), self.recursive(triangle, i+1, j+1))
