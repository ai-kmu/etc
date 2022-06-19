class Solution(object):
    def largestRectangleArea(self, heights):
        
        heights = [0] + heights + [0] 
        idx_stack = []
        
        max_rectangle = 0
        max_height = -1
        
        for i, height in enumerate(heights):
            
            # 이전값보다 증가했으면
            if height > max_height:
                idx_stack.append(i)
                max_height = height
                continue
                
            # 이전값보다 감소했으면
            elif  height < max_height:
                
                # 현재 높이보다 높이가 큰값 지우기
                while height < heights[idx_stack[-1]]:
                    global poped_idx
                    poped_idx = idx_stack.pop()
                    max_rectangle = max(heights[poped_idx]*(i-poped_idx), max_rectangle)
                    
                max_height = height
                heights[poped_idx] = max_height
                idx_stack.append(poped_idx)
            
        return max_rectangle
