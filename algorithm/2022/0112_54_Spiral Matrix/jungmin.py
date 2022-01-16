class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        tmp = matrix.copy() # 임시 행렬 tmp로 입력 matrix를 복사
        result = [] # 정답을 저장하는 리스트
        while len(tmp) != 0:
            result.extend(tmp[0]) # tmp의 0번째 행을 정답에 저장
            tmp.remove(tmp[0]) # 정답에 저장했으므로 tmp의 0번째 행 제거
            """
            tmp를 좌측 90도로 회전하면
            while문 돌 때 계속 tmp의 0번째 행을 저장하는 식으로 구현 가능하므로
            새로운 tmp는 이전 tmp에서 좌측 90도록 회전
            """
            list_of_tuples = zip(*tmp)
            rot_tmp=[]
            for i in list_of_tuples:
                rot_tmp.append(list(i))
            tmp = rot_tmp[::-1]
            
        return result
