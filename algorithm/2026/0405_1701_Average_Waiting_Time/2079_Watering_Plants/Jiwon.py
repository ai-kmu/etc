class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        if len(plants) == 1:
            return 1
        
        steps = 0
        cap = capacity

        for i, water in enumerate(plants):
            if cap < water:
                steps += 2*i  # 돌아가서 물 담기
                cap = capacity  # 물 리셋
            # 물 줄 수 있으면 가서 물 주기
            steps += 1
            cap -= water
        
        return steps
