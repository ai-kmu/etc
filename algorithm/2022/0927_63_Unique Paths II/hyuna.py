# 타임 리밋
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        # recursion을 이용하여 풀이 
        def recursive(i, j):
            # i, j 값이 그리드보다 커지거나 장애물을 만났을 경우 길이 막힘
            if i >=m or j>=n or obstacleGrid[i][j] == 1:
                return 0
            
            # 도착 지점까지 도착했을 때 1 더해줌 
            if i == m-1 and j == n-1:
                return 1
            
            # 오른쪽과 아래쪽으로 이동
            return recursive(i+1, j) + recursive(i, j+1)
        
        # 0,0 부터 시작 
        return recursive(0,0)
