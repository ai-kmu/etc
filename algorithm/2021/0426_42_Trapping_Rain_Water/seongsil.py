# 현재 블럭을 기준으로 왼쪽에 있는 블럭의 max 길이, 오른쪽에 있는 max 길이 중 작은 값에 현재 블록을 뺀값이
# 현재 블록 다음에 차오를 물의 부피가 됨. 단, 음수일 경우는 물이 차오르지 못하므로 음수인 경우는 제외

class Solution:
    def trap(self, height: List[int]) -> int:
        
        total_unit = 0
        
        for i in range(1, len(height) - 1):
            curr_unit = min(max(height[:i]), max(height[i+1:])) - height[i]
            if curr_unit > 0:
                total_unit += curr_unit
        
        return total_unit
