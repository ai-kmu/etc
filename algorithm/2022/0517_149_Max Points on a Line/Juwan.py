class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        def gcd(dx, dy):
            
            while(dy):
                
                dx, dy = dy, dx % dy
                
            return dx
        
        ans = 1
        
        for i in range(len(points)):
            max_points = defaultdict(lambda :1)
            for j in range(i+1, len(points)):
                
                
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                d_x = x1 - x2
                d_y = y1 - y2
                
                g = (0, 0)
                
                if d_x == 0:
                    g = (0, 0)
                elif d_x == 0:
                    g = (float("inf"),float("inf"))
                
                else:
                    if d_x < 0:
                        d_x, d_y = -d_x, -d_y
                    tmp = gcd(d_x, d_y)
                    g = (d_x/tmp, d_y/tmp)
                
                max_points[g] += 1
                ans = max(ans,max_points[g])
        return ans
