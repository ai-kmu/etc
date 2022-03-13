class Solution:
    def maxArea(self, height):
        Area=0
        
        lb = 0               # lower bound
        ub = len(height) - 1 # uppder bound
        
        # Binary Search
        while lb < ub:
            temp = (ub - lb) * min(height[lb], height[ub])
            Area = max(temp, Area)
            
            if height[lb] <= height[ub]:
                lb += 1
            else:
                ub -= 1
                
        return Area        
