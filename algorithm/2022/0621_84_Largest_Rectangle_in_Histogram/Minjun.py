# 실패한 코드 
# 최소값 기준 횡 최대값 구하다가 멈춤. . .

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        index = []
        h_max = 0
        stack.append(heights[0])
        index.append(heights[0])
        for i,v in enumerate(heights):
            while stack and stack[-1] > v:
                stack.pop()
                index.pop()
            stack.append(v)
            index.append(i)
            
        for i,v in enumerate(stack[:-1]):
            wid = v * ((len(heights)- index[i]))
            if h_max < wid:
                h_max = wid
        print(h_max)
