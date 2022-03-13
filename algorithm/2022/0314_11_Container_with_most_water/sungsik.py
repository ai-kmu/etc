class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 모든 경우의 수를 다 구하는 brute-force는 O(n^2)
        # start case를 처음과 끝으로 정하고 양 끝을 안으로 옮기는 방식으로 진행해야 함
        # left를 한칸 오른쪽으로 이동할지, right를 한칸 왼쪽으로 이동할지 정해야 하는데
        # 만약 height[left]가 height[right]보다 크다고 하면 물의 양은 height[right]에 의해 결정되고 있음
        # 이런 상황에서 left를 오른쪽으로 옮겨봤자 물의 양이 더 많아지는 것은 불가능 함
        # 따라서 right를 왼쪽으로 옮겨 물을 더 많이 담을 수 있을지 찾는다.
        
        def getAmount(l, r):
            return (r-l) * min(height[l], height[r])
        
        left, right = 0, len(height)-1
        amount = getAmount(left, right)
        
        while left < right:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
            
            amount = max(amount, getAmount(left, right))
            
        return amount
                    
