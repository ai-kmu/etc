class Solution:
    def maxArea(self, height: List[int]) -> int:
        # heigh가 담긴 arr
        # (i, 0) - (i, height[i])
        n = len(height)
        answer = 0
        
        # O(n^2) 시간초과
        # i부터 max 
        # for i in range(n-1):
        #     for j in range(i, n):
        #         store = min(height[j], height[i]) * (j-i)
        #         answer = max(store, answer)
        
        # greedy로 풀어야함
        left = 0
        right = n - 1
        while left < right: # 양쪽에서 이동
            # left와 right 사이의 영역 계산
            area = (right - left) * height[left] if height[left] < height[right] else (right - left) * height[right]
            
            # area와 answer 중 큰 값 선택
            answer = max(area, answer)
            if height[left] < height[right]: # right보다 left가 더 작다면 left가 이동
                left += 1
            else:
                right -= 1
        
        
        
        return answer
