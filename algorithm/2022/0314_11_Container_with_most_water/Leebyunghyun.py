class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        
        max_vol = 0
        
        while True:
            h = min(height[left_index], height[right_index])
            w = right_index-left_index
            tmp_vol = h*w
            max_vol = max(max_vol, tmp_vol)
            
            if left_index+1 == right_index:
                break
            
            # 문제 제시 조건: 너비*높이, 높이는 양쪽을 비교해서 더 낮은 쪽이 높이가 됨
            # 높은 쪽을 남겨가면서 폭을 줄여가며 부피를 검사
            if height[left_index]> height[right_index]:
                right_index-=1
            elif height[left_index] <= height[right_index]:
                left_index+=1
                
        return max_vol
            
