class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        
        # 이분 탐색
        # 최소 바나나 개수 l과 최대 바나나 개수 r을 더한 후 절반을 나눈 값을 mid로 함
        # 각 piles 안 요소들에 구한 mid를 나누어서 필요한 시간 hours를 구함
        # hours가 h보다 작거나 같으면 r을 이분 탐색 방법에 의해 갱신
        # hours가 h보다 크면 l을 갱신
        # l이 r보다 큰 순간 r+1을 리턴하여 최소 k값을 출력
        
        while l<=r:
            mid = (l+r) // 2
            hours = sum(((i-1)//mid) + 1 for i in piles)
            
            if hours <= h:
                r = mid-1
                
            else:
                l = mid+1
                
        return r+1
