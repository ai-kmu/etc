class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step = 0
        tmp = 0
        remain  = capacity

        for i in range(len(plants)):
            step += 1
            if remain < plants[i]:
                tmp += 2 * i
                remain = capacity
            
            step += tmp
            tmp = 0
            remain -= plants[i]

        return(step)
