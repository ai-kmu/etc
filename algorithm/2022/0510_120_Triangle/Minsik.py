class Solution:
    # Top-down 방식 진행 
    def minimumTotal(triangle):
        
        ## 한개만 있을 경우 대비: 
        if len(triangle) == 1:
            return triangle[0][0]

        ## 변수 정의
        rows = len(triangle)
        result = [[0 for x in row] for row in triangle]
        result[0][0] = triangle[0][0]

        ### Top-down 방식 탐색
        for row in range(1, rows, 1):
            num = len(triangle[row])

            for column in range(0, num, 1):

                # 맨 앞부분은 이전 행의 첫번째 값만 확인(해당 값 기준 오른쪽만 값 존재)
                if not column:
                    result[row][0] = result[row-1][0] + triangle[row][0]
                    
                # 맨 뒷부분은 이전 행의 마지막 값만 확인(해당 값 기준 왼쪽만 값 존재)
                elif column == (num - 1): 
                    result[row][-1] = result[row-1][-1] + triangle[row][-1]
                
                # 중간 부분은 이전 행의 앞과 뒷 부분의 값을 비교해서 작은값과 traingle 위치 값을 더함
                else:
                    result[row][column] = min(result[row-1][column], result[row-1][column-1]) + triangle[row][column]
        
        # 마지막 row의 대한 result 값의 경우 => path를 따라서 온 최소값들이 계산됨(이중에 최소값이 triangle의 최소값)
        return min(result[-1])
