''' 포인터를 두개로 두고 양끝에서부터 동시 비교하는 식으로 해결'''

class Solution:
    def maxArea(self, height):
        maxx = 0 # max 면적을 저장할 변수
        left = 0 # 포인터 1
        right = len(height) - 1 # 포인터 2
        
        while right > left:
            # 가로 길이(x축 방향)는 두 포인터의 차
            # 높이(y축 방향)는 두 높이중 더 낮은 높이로 한다.(높으면 물이 넘치게되니까)
            # 면적(area) = 가로 길이 x 높이
            area = (right - left ) * min(height[left] , height[right])
        
        # 짧은 높이를 기준으로 물이 담기니까 짧은 포인터를 옮겨야 면적을 넓힐 가능성이 있다.
        # 그래서 right와 left 중 더 짧은 포인터를 옮긴다.
        #즉, 더 짧은 쪽이 left 라면 left+1, right라면 right-1
            if height[right]< height[left]:
                right -=1
            else:
                left +=1

            maxx= max(maxx, area)
        return maxx
