# 다음 과정을 두번째 줄부터 마지막 줄까지 반복
# i번째 줄에 첫번째 숫자에는  i-1번쨰 줄에 첫번째 숫자를 더함
# i번째 줄에 마지막 숫자에는  i-1번쨰 줄에 마지막 숫자를 더함
# 나머지의 경우 i번째 줄에 k번째 수에는 i-1번째 줄의 k-1과 k번째 수중 작은 것을 더함

# 마지막 줄까지 위 연산을 적용 후 마지막 줄에서 가장 작은 숫자 출력



class Solution:
    def minimumTotal(self, triangle):
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            for j in range(1, i):
                triangle[i][j] += min((triangle[i-1][j-1], triangle[i-1][j]))
            triangle[i][-1] += triangle[i-1][-1]
            
        return min(triangle[-1])
    
