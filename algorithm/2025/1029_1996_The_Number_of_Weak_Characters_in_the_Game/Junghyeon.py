import heapq


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: (x[0], -x[1]))
        queue = []
        weak = 0

        for i in range(len(properties)):
            while queue and queue[0][0]<properties[i][1] and queue[0][1]<properties[i][0]:
                weak+=1
                heapq.heappop(queue)
            heapq.heappush(queue, (properties[i][1], properties[i][0]))
        
        return weak
