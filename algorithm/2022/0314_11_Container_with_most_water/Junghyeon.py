class Solution:
    '''
    투 포인터를 이용해서 최대 넓이를 업데이트
    '''
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        
        # 넓이의 세로길이는 두개의 포인터 중 작은 값이 결정
        while l < r:
            area = (r - l) * min(height[l], height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            max_area = max(max_area, area)
            
        return max_area
