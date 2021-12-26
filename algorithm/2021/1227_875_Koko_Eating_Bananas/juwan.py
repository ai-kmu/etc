class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 문제에 대해서 설명하자면, koko라는 원숭이는 바나나를 최대한 천천히 먹고싶은데, 경비원이 다시 돌아오기 전까지는
        # 모든 바나나를 먹는 것이 목표.
        # 따라서 최대한 천천히 먹을 수 있는 시간과 경비원이 돌아오는 시간을 둘 다 만족해야함.
        # 바나나를 piles에 있는 max값으로 먹는다면, h의 값 범위가 piles의 리스트 길이보다 크기 때문에 항상 다 먹을 수 있지만
        # 최대한 천천히 먹지 못함. 반대로 1시간에 1개만 먹으면 그 사이에 경비원이 무조건 돌아올 것.
        # 그렇다면 1 에서 max(piles) 사이에 조건을 만족하도록 이진 탐색이 가능함. 
        
        left, right = int(sum(piles)/h) or 1, max(piles) # 이진 탐색의 범위
        
        while left < right: # 이진 탐색 시작
            mid = (left+right) // 2 # 중앙값 계산
            if sum([ceil(bananas / mid) for bananas in piles]) > h:
                # 이진 탐색한 값으로 각 바나나를 다 먹었을 때 걸리는 시간 계산. 
                # 다 먹기 전에 경비원이 오면
                left = mid+1
                # 시간 당 먹는 양을 늘림
            else:
                right = mid
                # 그게 아니라면, 시간 당 먹는 양을 줄여서 더 천천히 먹으려고함.
        # 이진 탐색이 끝나면 최적의 값을 반환해줄 것
        return left
    
