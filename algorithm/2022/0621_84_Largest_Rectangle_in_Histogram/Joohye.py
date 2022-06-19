# 오답 코드

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        # n개의 1로 초기화해서 풀이 시도
        n = len(heights)
        left = [1]*n
        right = [1]*n
        
        for i in range(1,n):
            j = i - 1
            #이전 바의 높이가 현재바의 높이보다 높을때
            while j >= 0 and heights[j] >= heights[i]:
                j -= left[j]
            left[i] = i - j

        for i in range(n-2,-1,-1):
            j = i + 1
            # 높이의 길이보다 작고, 이후 바의 높이가 현재바의 높이보다 높을떄
            while j < n and heights[i] <= heights[j]:
                j += right[j] 
            right[i] = j - i
            
        res = 0
        res = max(res,heights[i]*(left[i]+right[i]))
        return res
    
