# 발표자 comment
# PEP(Python Enhancement Proposal)
# +=사용시 좌우로 space 한칸씩 띄면 좋습니다.
# 물론 안띄어도 되긴 합니다만 권장사항입니다.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        maxrow = len(matrix) -1
        maxcol = len(matrix[0]) -1
        
        minrow = 0
        mincol = 0

        #행렬의 전체 원소의 수
        size = len(matrix) * len(matrix[0])
        count = 0
        
        while(count < size):
            
            #윗줄의 왼쪽에서 오른쪽으로 숫자를 가져옴
            for j in range(mincol,maxcol+1):
                if(count<size):
                    answer.append(matrix[minrow][j])
                    count +=1
            #윗쪽 줄을 한칸 줄임
            minrow +=1
            
            #오른쪽 줄 위부터 아래로 숫자를 가져옴
            for i in range(minrow,maxrow+1):
                if(count<size):
                    answer.append(matrix[i][maxcol])
                    count +=1
            #오른쪽 줄을 한칸 줄임
            maxcol -=1
            
            #아랫쪽 줄 오른쪽부터 왼쪽으로 숫자를 가져옴
            for j in range(maxcol,mincol-1,-1):
                if count<size:
                    answer.append(matrix[maxrow][j])
                    count +=1
            #아래쪽 줄을 한칸 줄임        
            maxrow -=1
            
            #왼쪽줄 아래서부터 윗쪽으로 숫자를 가져옴
            for i in range(maxrow,minrow-1,-1):
                if(count<size):
                    answer.append(matrix[i][mincol])
                    count +=1
            #왼쪽 줄을 한칸 줄임        
            mincol +=1
            
        return answer
