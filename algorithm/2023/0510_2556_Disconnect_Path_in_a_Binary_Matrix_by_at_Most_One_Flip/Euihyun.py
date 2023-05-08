# 못풀었습니다.
# 정답보고 공부한 코드로 리뷰안해주셔도 됩니다.

class Solution(object):
    def isPossibleToCutPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m, n = len(grid), len(grid[0])  # 그리드의 크기 구하기
        
        # 문제 해결을 위한 재귀 함수 정의
        def solve(i, j):
            # 만약 현재 위치가 끝점이면
            if(i == m-1 and j == n-1):  
                # True 반환
                return True  
            # 만약 현재 위치가 그리드의 범위를 벗어나거나 0이면    
            if(i == m or j == n or grid[i][j] == 0):  
                # False 반환
                return False  
            # 시작점이 아니라면 현재 위치를 0으로 바꿔줌 (나중에 뒤돌아갈 때 방지하기 위해)    
            if(i + j): grid[i][j] = 0  
            # 현재 위치에서 아래로 가는 경우와 오른쪽으로 가는 경우 모두 시도해봄
            return solve(i + 1, j) or solve(i, j + 1)  
        # 만약 시작점에서 끝점까지 경로가 하나뿐이라면 (즉, 뒤집어도 같은 경로가 나오는 경우)
        if(not solve(0, 0)):  
            # True 반환
            return True  
        # 만약 시작점에서 끝점까지 경로가 두 개 이상이라면 (즉, 뒤집어도 다른 경로가 나오는 경우)
        if(not solve(0, 0)):  
            # True 반환
            return True  
        # 모든 경우가 아니면 False 반환    
        return False  
