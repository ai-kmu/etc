class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        rest = capacity
        ret = 0

        for i in range(len(plants)):
            if rest < plants[i]:
                ret += (2*i + 1)
                rest = capacity

            else:
                ret += 1
            
            rest -= plants[i]

        return ret
