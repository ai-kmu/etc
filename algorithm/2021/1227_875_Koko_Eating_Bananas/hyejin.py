class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 바나나를 먹는 속도
        # 한시간에 k개를 먹음
        # k개보다 작다면 다 먹고, 그 1시간동안 움직일 수 없음.
        # k는 1개부터 max 바나나 개수까지 가능
        # k의 최솟값 찾기
        
        left, right = 1, max(piles)+1
        
        # k를 binary search로 찾음
        while left < right:
            mid = (left+right) // 2
            answer = 0
            
            for pile in piles:
                answer += math.ceil(pile / mid)
            if answer > h:
                left = mid + 1
            else:
                right = mid
        
        return left
        
