# 발표자 comment
# +=을 이용해 한번에 추가하는 것이 좋을듯 합니다.
# return이 없습니다.

'''
while 문과 for문을 이용하여 하나씩 읽었다.
일단 4가지 방향을 설정한 다음,
한 방향씩 읽을 때마다 범위를 줄였다.
원소를 읽으면서 res라는 리스트에 하나씩 넣었다.

맨위에서 왼쪽부터 오른쪽으로 읽으면
top을 +1하였다.
오른쪽 부분 맨 위 부터 맨아래까지 읽으면
right를 -1을 하였다. (읽을 필요가 없기 때문)
그다음 맨아래 원소를 오른쪽에서 왼쪽으로 읽고 
마지막행은 다 읽었기 때문에 bottom에서 -1을 하고 
마지막행의 왼쪽 원소의 맨 아래부터 맨위로 읽고
왼쪽원소는 다 읽었으므로 left에서 +1을 하였다.

left가 right 크기의 이상이면서
top이 bottom 크기 이상일때,
더이상 읽을 원소가 없기 때문에
if not()을 이용해 break를 하였다.

'''



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        left, right=0, len(matrix[0])#len(matrix[0])은 열의 길이를 반환
        top, bottom=0, len(matrix)#len(matrix)는 행의 길이를 반환
        while left<right and top<bottom: #break되는 조건
            for i in range(left, right): #왼쪽에서 오른쪽으로 읽기
                res.append(matrix[top][i])
            top +=1 #읽기가 끝나면 0행에서 1행으로 행을 더해야함.
            
            #오른쪽 맨 위에서 맨 아래로 읽기
            for i in range(top, bottom):
                res.append(matrix[i][right-1]) 
                #맨 오른쪽 원소는 len(matrix[0])-1이다. out of range 방지
            right -=1
            
            #break조건
            if not (left<right and top<bottom  ):
                break
            #오른쪽에서 왼쪽으로 거꾸로 읽기
            for i in range(right-1, left-1, -1): #왼쪽을 포함 하기위해 left-1
                res.append(matrix[bottom-1][i])
            bottom -=1
            
            
            for i in range(bottom-1, top-1,-1):
                res.append(matrix[i][left])
            left +=1
