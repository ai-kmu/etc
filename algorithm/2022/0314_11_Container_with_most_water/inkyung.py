class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 왼쪽과 오른쪽에서 비교하면서 가장 최대의 크기 찾기
        left, right = 0, len(height) - 1
        area = 0
        
        # 양쪽에서 비교
        while left < right:
            water = (right - left) * min(height[left], height[right])
            # 가장 큰 값을 찾으면서 비교해야하기 때문에 값이 작으면 옮겨가기
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            area = max(area, water)
        return area
