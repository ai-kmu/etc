# 66 / 98 test cases passed.
def largestRectangleArea(heights):
        # stack을 이용
        ans = 0
        stack = []
        
        # 왼쪽부터 하나씩 처리하면서 최대 넓이를 계산
        for i in range(len(heights)):
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                
                if len(stack) == 0:
                    width = i
                else:
                    width = i - index
                ans = max(ans, width * height)
            stack.append((i,heights[i]))
        
        # 스택에 남은 것들을 처리
        while stack:
            index , height = stack.pop()
            
            if len(stack) == 0:
                width = len(heights)
            else:
                width = len(heights) - index
            ans = max(ans, width * height)
        
        return ans