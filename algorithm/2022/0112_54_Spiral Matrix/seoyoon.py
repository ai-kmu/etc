# 발표자 comment
# 주석은 보통 위에 다는것이 일반적입니다.
# list를 만들어 놓고 +=을 이용해 한번에 추가하는 것이 시간적으로 이득입니다.


# 양파껍질을 벗겨내는 방식으로 접근
# 즉, 가장 바깥쪽 layer을 모두 순화하고, 안쪽 layer을 순화하는 방식

class Solution:
    def spiralOrder(self, matrix):
        result = [] # 결과를 저장할 빈 리스트 생성

        while matrix: #(A)
            result += matrix.pop(0) 
            # (A): 맨 위쪽 껍질 벗기는 단계
            # pop(0)으로 첫번째 행을 뽑아서 result에 추가한다

            if matrix and matrix[0]: #(B)
                for row in matrix:
                    result.append(row.pop())
            # (B): 오른쪽 껍질을 벗기는 단계
            # for문에서 row는 List단위이고 그 중에서 가장 오른쪽 값이 필요하니까
            # pop()을 통해 각 행의 가장 마지막 요소를 뽑아와서 result에 추가
            
            if matrix: #(C)
                result += matrix.pop()[::-1] 
            # (c): 아래쪽 껍질을 벗기는 단계
            # 맨 아래쪽 행을 pop()으로 뽑고, 
            # 이 list의 원소들이 역순으로 추가되어야 하니까 [::-1]인덱싱으로 값을 뒤집어준다

            if matrix and matrix[0]: #(D)
                for row in matrix[::-1]:
                    result.append(row.pop(0))
             # (D): 왼쪽 껍질을 벗기는 단계
             # 오른쪽 껍질을 벗길 때의 순서와 반대이다.
             # 행들을 먼저 역순으로 불러오고 
             # list의 가장 앞 원소를 pop(0)을 통해 뽑아내서 result에 넣는다

             # while 반복문을 통해 위 과정을 반복하고 matrix가 빈 list가 될 때 반복문을 탈출한다.
            
        return result
    
    
    """
    matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]] 일 때 
    (A),(B),(C),(D) 각 단계별 결과 예시
    
    (A) 
    matrix = [[5, 6, 7, 8],[9, 10, 11, 12]] 
    result= [1,2,3,4]
    
    (B)
    matrix = [[5, 6, 7], [9, 10, 11]]
    result = [1, 2, 3, 4, 8, 12]
    
    (C)
    matrix = [[5, 6, 7]]
    result =  result = [1, 2, 3, 4, 8, 12, 11, 10, 9]
    
    (D)
     matrix = [[6, 7]]
     result = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5]
    
    (A)
    matrix = []
    result =  [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    """
    
#pop() vs pop(0)
#pop(): list의 마지막 요소 뽑아냄
#pop(0): list의 첫 번째 요소 뽑아냄
