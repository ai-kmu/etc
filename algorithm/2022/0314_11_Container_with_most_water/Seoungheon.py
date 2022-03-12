class Solution(object):
    def maxArea(self, height):

        # 왼쪽과 오른쪽의 값을 구해서 현재 구할수 있는 최대크기를 구하고 height가 작은쪽을 한칸씩 이동하며 최대크기구하는것을 반복한다.
        
        left = 0
        right = len(height)
        max_size = 0
        cur_weight = len(height)
        
        while left != right :
            left_height = height[left]
            right_height = height[right-1]
            
            # 최대크기 계산
            cur_height = min(left_height, right_height)
            cur_weight -= 1
            max_size = max(cur_height*cur_weight, max_size)
            
            # height 가 작은 쪽을 한칸 이동
            if left_height > right_height :
                right -= 1
            else :
                left += 1
              
        return max_size
