# 발표자 comment
# PEP(Python Enhancement Proposal)에 따라 if문 구절이나 while문 구절이 끝나면 한줄 띄워주세요
# P.S 주석 쩌네요
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        top=0
        bottom=len(matrix)-1
        left=0
        right=len(matrix[0])-1
        """
        각 포인터 개념으로 설정한 것들.
        아래 while문과 for문을 사용해서
        그림에 나오는 것처럼 넣어주는 방식과 동일.
        """
        
        
        
        size=len(matrix) * len(matrix[0])
        arr=[]
    while len(arr)<size:
        if len(arr)<size:
            for i in range(left,right+1):
                arr.append(matrix[top][i])
            top+=1
        """
        _________________
        |-------------->|
        |               |
        |               |
        |               |
        |               |
        -----------------
        """
        if len(arr)<size:
            for i in range(top,bottom+1):
                arr.append(matrix[i][right])
            right-=1
        """
        _________________
        |              ||
        |              ||
        |              ||
        |              ||
        |              v|
        -----------------
        """
        if len(arr)<size:
            for i in range(right,left-1,-1):
                arr.append(matrix[bottom][i])
            bottom-=1
        """
        _________________
        |               |
        |               |
        |               |
        |               |
        |<--------------|
        -----------------
        """
        if len(arr)<size:
            for i in range(bottom,top-1,-1):
                arr.append(matrix[i][left])
            left+=1
        
        """
        _________________
        |               |
        |^              |
        ||              |
        ||              |
        ||              |
        -----------------
        """
        print(arr)
    return arr
  
  
  """
  그냥 while문 한번이 한 싸이클이라 생각하면 편함.
  
  """
