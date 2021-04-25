class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1      # 양쪽 포인터
        
        l_max = r_max = 0      # 양쪽 벽 높이
        ans = 0
        while l < r:           
            if height[l]<height[r]:     # 양쪽 포인터 번갈아가면서 업데이트
                if height[l] >= l_max:  # max값 업데이트
                    l_max = height[l]
                else:                   # max보다 작으면 물값 더하기
                    ans += l_max-height[l]
                l += 1    # left pointer는 오른쪽으로 한칸씩
            else:
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    ans += r_max-height[r]
                r -= 1    # right pointer는 오른쪽으로 한칸씩
        
        return ans
