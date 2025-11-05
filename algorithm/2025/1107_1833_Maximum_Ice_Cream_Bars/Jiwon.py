class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
      # 가진 돈이 더 많거나 아이스크림 가격과 같다면 전부 살 수 있음  
      if sum(costs) <= coins:
            return len(costs)

        # 가능한 많이 사야함: 정렬해서 저렴한 순서대로 담기
        costs.sort()
        ans = 0
        for cost in costs:
            if cost <= coins:
                coins -= cost
                ans += 1
            else:
                break
        
        return ans
