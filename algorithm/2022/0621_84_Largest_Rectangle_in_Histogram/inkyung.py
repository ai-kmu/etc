class Solution(object):
    def largestRectangleArea(self, heights):
        heights.append(-1)  # 마지막값도 확인할 수 있도록 빈값 하나 추가
        
        max_area = max(heights)
        stack = []
        
        for i in range(len(heights)):
            idx = i
            # 현재보다 stack의 쌓인 높이보다 큰게 나왔다면 -> 최대 넓이를 갱신할 수 있음
            while stack and stack[-1][1] >= heights[i]:
                idx, height = stack.pop()
                # print(idx, height, heights[i])
                width = i - idx
                
                max_area = max(max_area, height * width)
                
            stack.append((idx,heights[i]))
            
        return max_area  
