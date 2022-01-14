class Solution:
    '''
    문제풀이 방법
    1. matrix의 첫번째 row를 모두 리턴값인 answer에 저장
    2. 이미 저장된 값들을 뺀 새로운 matrix를 생성 후 왼쪽으로 90도 회전
    3. matrix가 비어있을때까지 loop를 반복
    '''
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = list()

        # matrix가 비어있을때까지 반복
        while True:
            # matrix의 첫번째 row를 answer에 삽입
            for i in range(len(matrix[0][:])):
                answer.append(matrix[0][i])

            # 이미 삽입된 첫번째 row를 삭제한 새로운 matrix 생성    
            matrix = matrix[1:][:]
            
            # Loop 종료 조건
            if len(matrix) == 0:
                break

            # matrix를 왼쪽으로 90도 회전시키는 알고리즘
            row = len(matrix)
            col = len(matrix[0])
            new_matrix = [[0] * row for _ in range(col)]
            for i, rv_i in enumerate(range(col-1, -1, -1)):
                for j in range(row):
                    new_matrix[rv_i][j] = matrix[j][i]
            matrix = new_matrix

        return answer
