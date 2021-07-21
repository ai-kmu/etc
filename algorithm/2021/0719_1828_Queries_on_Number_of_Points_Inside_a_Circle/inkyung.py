class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = []
        
        for cir in queries:
            temp = 0
            x, y, r = cir[0], cir[1], cir[2]
            
            for p in points:
                # 원 안에 있는지 확인
                if (p[0] - x)**2 + (p[1] - y)**2 <= r**2:
                    temp += 1
            answer.append(temp)
        return answer
