class Solution(object):
    def maxArea(self, height):

        # 왼쪽과 오른쪽의 값을 구해서 현재 구할수 있는 최대크기를 구하고 height가 작은쪽을 한칸씩 이동하며 최대크기구하는것을 반복한다.
        
        left_i = 0
        right_i = len(height)
        max_size = 0
        cur_weight = len(height)
        
        while True :
            left_height = height[left_i]
            right_height = height[right_i-1]
            
            # 최대크기 계산
            cur_height = min(left_height, right_height)
            cur_weight -= 1
            max_size = max(cur_height*cur_weight, max_size)
            
            # height 가 작은 쪽을 한칸 이동
            if left_height > right_height :
                right_i -= 1
            else :
                left_i += 1
            
            # 두 값이 같아지면 탈출
            if left_i == right_i :
                break
            
        return max_size
