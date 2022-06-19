from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # index와 height를 쌍으로
        
        for i, h in enumerate(heights):
            start = i
            
            # height[i]가 될 수 있는 것중 가장 작은 index 찾기
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                width = i - index
                temp_area = height * width
                # 'i' 전 증가한 넓이 계산
                max_area = max(max_area, temp_area)
                start = index
            
            stack.append((start, h))
        
        # stack의 남은 부분도 계산
        for i,height in stack:
            width = len(heights) - i
            temp_area = height * width
            max_area = max(max_area, temp_area)
            
        return max_area
        
height1 = [2,1,5,6,2,3]
height2 = [2,4]
height3 = [2,1,2]
a = Solution()

print(a.largestRectangleArea(height1))
print(a.largestRectangleArea(height2))
print(a.largestRectangleArea(height3))
