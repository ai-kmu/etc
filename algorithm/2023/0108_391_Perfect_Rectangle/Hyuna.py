import math
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        # rectangles의 최소 최대 x y지점을 찾아서 구한 최대 넓이와
        # 하나의 사각형의 넓이들을 모두 구해 값을 비교하여 같지 않을 때 false를 리턴 

        minx = math.inf 
        miny = math.inf 
        maxx = -math.inf 
        maxy = -math.inf    
        totalArea = 0    

        for rect in rectangles:
            leftx = rect[0]
            lefty = rect[1]
            rightx = rect[2]
            righty = rect[3]

            # 전체 넓이 구함 
            totalArea += ((rightx-leftx) * (righty - lefty))

            # 최대 최소 x y값 갱신 
            if leftx < minx:
                minx = leftx
            
            if rightx > maxx:
                maxx = rightx
            
            if lefty < miny:
                miny = lefty
            
            if righty > maxy:
                maxy = righty

        # 각 사각형의 최대 넓이 구하는 부분
        maxArea = ((maxx - minx) * (maxy - miny))
        
        # 넓이가 같지 않을 때 
        if maxArea != totalArea:
            return False
        
        return True


        
