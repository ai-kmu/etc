# 오답 코드 (문제 너무 어렵습니다..)
from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def getMin(l, r):
            minIdx = l
            minHeight = heights[l]
            flag = False
            for i in range(l+1, r+1):
                if heights[i] != minHeight:
                    flag = True
                if heights[i] < minHeight:
                    minHeight = heights[i]
                    minIdx = i

            return flag, minIdx, minHeight
        
        area = max(heights)
        queue = deque([(0, len(heights)-1)])
        
        while queue:
            l, r = queue.popleft()
            flag, minIdx, minHeight = getMin(l, r)
            area = max(area, (r-l+1) * minHeight)
            if not flag:
                continue
            if minIdx < r:
                queue.append((minIdx+1, r))
            if l < minIdx:
                queue.append((l, minIdx-1))
            
        return area
            
