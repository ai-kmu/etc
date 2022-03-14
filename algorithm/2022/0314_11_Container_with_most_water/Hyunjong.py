class Solution(object):
    def maxArea(self, height):
        ans = 0
        num_height = len(height)
        left_point = 0
        right_point = num_height - 1
        # 포인터 2개 사용해서 푸는 방법
        while left_point < right_point:
            short = min(height[left_point], height[right_point])
            #짧은 높이 구하고 
            ans = max(ans, short * (right_point - left_point))
            #면적 구해서 가장 넓은 면적을 찾는 방법
            
            if height[left_point] < height[right_point]:
            # 왼쪽과 오른쪽 중에서 더 짧은 포인터 옮기기
                left_point += 1
            else:
                right_point -= 1
        return ans
