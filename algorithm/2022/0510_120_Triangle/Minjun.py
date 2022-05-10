''' 
feedback 정리
-> h 변수 이름이 명확하지가 않다  h 뜻 보다는 height로 해주자
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        h = len(triangle)
        
        for i in range(1, h):
            for j in range(len(triangle[i])):
                # 첫번째는 이전 첫번째 + 현재
                if j == 0 :
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j]
                # 마지막은 이전 마지막 + 현재
                elif j == i:
                    triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
                # 아닌 경우 위 2개 값 중 작은 값 + 현재
                else:
                    triangle[i][j] = triangle[i][j] + min(triangle[i-1][j-1],triangle[i-1][j])
        
        # 갱신한 값 중 제일 작은 값
        return min(triangle[-1])
