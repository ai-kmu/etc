from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        answer = 1
        lines = defaultdict(dict)
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1, p2 = points[i], points[j]
                x1, y1, x2, y2 = p1[0],p1[1],p2[0],p2[1]
                
                line = (x1)
                # 다르다면 gradient 계산
                if x2 != x1:
                    gradient = (y2 - y1) / (x2 - x1)
                    n_line = y2 - gradient * x2
                    
                    line = (gradient, n_line)
                
                lines[line][i] = lines[line][j] = 1
                answer = max(answer, len(lines[line].keys()))
                print(lines)
        return answer
