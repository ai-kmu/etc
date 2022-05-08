class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # index 1부터 top down 방식으로 더해나가는 방식
        for i in range(1, len(triangle)):
            # 첫번째 인덱스의 값은 이전 단계의 값들 중 0에 해당하는 값을 더해서 업데이트
            triangle[i][0] += triangle[i-1][0]
            # 만약 한 인덱스에 더해질 수 있는 숫자가 2개라면 둘 중 작은 것을 더해줌
            for j in range(i-1):
                triangle[i][j+1] += min(triangle[i-1][j], 
                                        triangle[i-1][j+1])
            # 현재 인덱스의 리스트들 중 마지막 값은 이전 인덱스의 마지막 값을 더해서 업데이트
            triangle[i][-1] += triangle[i-1][-1]
        # 업데이트 된 triangle의 마지막 리스트 중 가장 작은 값을 반환
        return min(triangle[-1])
