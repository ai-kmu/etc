class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        full = capacity
        for i, p in enumerate(plants):
            if capacity - p >= 0:
                steps += 1
                capacity -= p
            else:
                # 강으로 
                steps += i
                capacity = full
                # 다음으로 가기
                steps += i+1
                capacity -= p
        return steps
