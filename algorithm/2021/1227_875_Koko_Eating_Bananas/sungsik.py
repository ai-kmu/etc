class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 속도 k가 주어지면 바나나를 다 먹는데까지 걸리는 시간을 계산
        def getHours(k):
            hours = [(pile-1) // k + 1 for pile in piles]
            return sum(hours)
        
        # k의 최솟값, 최댓값은 각각 1, piles의 최댓값이다.
        # 이 문제는 1 ~ max(piles)의 범위에서 
        # 최소한의 검색을 통해 최적화된 속도 k를 찾는 문제이다.
        minK, maxK = 1, max(piles)
        
        # first phase
        # 우선, 가능한 시간을 최대한 사용해야 하기 때문에
        # 시간이 h가 되는 k를 찾는다.
        # k가 커질수록 걸리는 시간은 그에 반비례하기 때문에
        # binay search 방식을 적용해
        # 걸리는 시간이 h가 될 때까지 찾는다.
        while minK <= maxK:
            midK = (minK + maxK) // 2
            hours = getHours(midK)
            
            if hours > h:
                minK = midK + 1
            elif hours < h:
                maxK = midK - 1
            # second phase
            # 걸리는 시간이 h가 되는 k는 유일하지 않다.
            # 따라서 걸리는 시간이 h가 되는 k들 중에서 최솟값을 찾아야 하기 때문에
            # 다시 binary search 방식을 적용해
            # 시간이 h만큼 걸리며, k에 1을 빼면 h보다 많이 걸리는 k를 찾는다.
            else:
                maxK = midK
                while minK < maxK:
                    midK = (minK + maxK) // 2
                    hours = getHours(midK)
                    if hours == h:
                        if getHours(midK-1) != h:
                            return midK
                        maxK = midK - 1
                    else:
                        minK = midK + 1
                return minK
        return minK
