# 탐색은 오른쪽 아래로
# 답을 찾는 것(주변에 1이 몇개인지 찾는 것)은 왼쪽 위로
# matrix 자체를 dp table로 사용, 탐색을 하면서 내 위치로 부터 왼쪽 위로 구성된 사각형에서 만들 수 있는 최대 사각형의 크기를 
# 저장하는 식임, 방법은 내 왼쪽, 위쪽, 대각선으로 왼쪽위를 탐색해 이중 가장 작은것에 1을 더해주면 됨

class Solution:
    def maximalSquare(self, matrix):
        matrix = [list(map(int,d)) for d in matrix] # type 변환
        
        # 탐색할시 (0,0)위치가 아닌 (1,1) 위치부터 시작할 것임 하지만 그렇게 하면 matrix[0, :]이나 matrix[:, 0]에만 1이 존재할 시 
        # 오류 발생의 여지가 있음
        ans = max(max(matrix[0]), max([d[0] for d in matrix]))
        
        for i in range(1, len(matrix)):
            for j in range(1,len(matrix[0])):
                matrix[i][j] *= (min((matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])) + 1)# 곱해주는 이유는 matrix[i][j]가 0이면 업데이트를 해주면 안되니까
                ans = max(matrix[i][j], ans)

        return ans ** 2
