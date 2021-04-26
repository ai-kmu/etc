class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if not height:
            return 0
        
        result = 0
        
        # left, right idx
        left = 0
        right = len(height)-1
        
        # left, right max height
        left_height = height[left]
        right_height = height[right]
        
        while left < right:
          # 현재 위치 기준으로 왼쪽 / 오른쪽 높이 최댓값 경신
            left_height = max(left_height, height[left])
            right_height = max(right_height, height[right])
            
            
            # left 높이가 right보다 작거나 같을 경우 left idx 이동
            if left_height <= right_height:
                result += left_height - height[left]
                left += 1
                
            else:
              # right idx 이동
                result += right_height - height[right]
                right -= 1
        return result
        
