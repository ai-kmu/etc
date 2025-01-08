## 테케 30에서 틀리고 모르겠음... 아래는 답봄 리뷰 안해줘도 됨요

class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        
        # 일단 90도 돌리고
        # 돌린거에서 열 기준으로 내려갈수 있는지 확인후 내려가기
        # 다 필요없고 현재 내 문자가 '#' 이면 오른쪽으로 더 갈수 있는지 확인하기

        n, m = len(boxGrid), len(boxGrid[0])
        
        for i in range(n):
            for j in range(m-1):
                if boxGrid[i][j] == '#' and boxGrid[i][j+1] == '.':
                    boxGrid[i][j+1] = boxGrid[i][j]
                    boxGrid[i][j] = '.'

        boxGrid_new = [[j for j in range(n)] for i in range(m)]

        
        for i in range(m):
            for j in range(n):
                boxGrid_new[i][j] = boxGrid[n-1-j][i]
                
        return(boxGrid_new)
                    
# 답 보

class Solution(object):
    def rotateTheBox(self, boxGrid):
        """
        :type boxGrid: List[List[str]]
        :rtype: List[List[str]]
        """
        
        n, m = len(boxGrid), len(boxGrid[0])

        for i in range(n):
            for j in range(m - 1, 0, -1): 
                if boxGrid[i][j] == '.' and boxGrid[i][j - 1] == '#':
                    boxGrid[i][j], boxGrid[i][j - 1] = boxGrid[i][j - 1], boxGrid[i][j]
        

        boxGrid_new = [[None for _ in range(n)] for _ in range(m)]
        for i in range(m): 
            for j in range(n): 
                boxGrid_new[i][j] = boxGrid[n - 1 - j][i]  # 90도 회전 공식
        

        return boxGrid_new

