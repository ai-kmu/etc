class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cur_cost = 0
        bar = 0

        while bar < len(costs):
            cur_cost += costs[bar]

            if cur_cost > coins:
                break

            bar += 1

        return bar
