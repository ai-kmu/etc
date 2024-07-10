#풀다가 정답 봐버렸음 리뷰 안해주셔도 됩니다.
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        # 매트릭스가 비어 있는지 확인
        if not mat: 
            return []
        
        len_row = len(mat)  
        len_col = len(mat[0])  
        
        result = []  
        row = col = 0  
        
        for i in range(len_row * len_col):
            result.append(mat[row][col])  
            
            # 현재 위치의 합이 짝수일 때 (대각선이 오른쪽 위로 이동)
            if (row + col) % 2 == 0:
                 # 열의 끝이면 행 증가
                if col == len_col - 1: 
                    row += 1
                # 첫번째 행에 있는 경우 열 증가
                elif row == 0:  
                    col += 1
                # 그냥은 행을 감소하고 열을 증가
                else:  
                    row -= 1
                    col += 1
            # 현재 위치의 합이 홀수일 때 (대각선이 왼쪽 아래로 이동)
            else:
                # 행의 끝이면 열 증가
                if row == len_row - 1:  
                    col += 1
                # 첫번째 열에 있는 경우 행 증가
                elif col == 0:  
                    row += 1
                # 그냥은 행을 증가하고 열을 감소
                else:  
                    row += 1
                    col -= 1   
        
        return result  

        
