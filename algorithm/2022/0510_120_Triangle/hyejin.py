class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        
        # 현재 위치에서 상위 level의 min을 더함. (각 자리에서의 minimum path를 구함)
        for i in range(1 , height):
            for j in range(i + 1):
                if 0 < j < i:
                    triangle[i][j] += min(triangle[i - 1][j - 1] , triangle[i - 1][j])
                elif j:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += triangle[i - 1][j]
        

        return min(triangle[-1])
