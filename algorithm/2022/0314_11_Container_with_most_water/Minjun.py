class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        이진탐색
        '''
        
        l = 0
        r = len(height)-1
        # 최대면적
        max_area = 0
        
        while(l < r):
            
            # 가로
            wid = r - l
            
            # 세로
            heit = min(height[l], height[r])
            
            # 넓이
            area = wid * heit
            
            # 최대면적
            max_area = max(max_area, area)
            
            # 현재 세로보다 더 큰 세로를 찾을 때까지 이동               
            while(l <= r and height[l] <= heit):
                l += 1
            
            while(l <= r and height[r] <= heit):
                r -= 1                
              
        return max_area
