class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        temp = set(map(tuple,rectangles)) # 중복된 사각형이 있는지 알아보기 위한 set
                                          # list 자체는 hashable하지 않아서 rectangle의 원소를 hashable한 tuple로 변환 후 set

        if len(rectangles) != len(temp):  # 만약 똑같은 사각형이 있으면 바로 False
            return False
        
        min_left, min_bot, max_right, max_top = float('inf'),float('inf'),float('-inf'),float('-inf')

        total_area = 0
        inner_points = defaultdict(int) # 각 Point들이 전체 사각형을 이루는데 얼만큼 찍혔는지 알아보기 위함
                                        # 완전한 사각형은 가장 바깥쪽 좌표를 제외한 나머지 좌표들은
                                        # 최소 2번이상 겹치는데, 짝수번으로 

        for l, b, r, t in rectangles:
            total_area += (r-l)*(t-b) # 작은 사각형의 넓이를 더해둠
                                      # 이후에 큰 사각형이 만들어졌을 때의 넓이와 비교할 것임
            inner_points[(l, b)] += 1 
            inner_points[(l, t)] += 1
            inner_points[(r, b)] += 1
            inner_points[(r, t)] += 1
            
            min_left = min(min_left, l) # 가장 큰 사각형의 좌표를 구해놓음
            min_bot = min(min_bot, b)
            max_right = max(max_right, r)
            max_top = max(max_top, t)

        if total_area != (max_right - min_left) * (max_top - min_bot): # 만약 넓이가 일치하지 않으면 False 리턴
            return False

        inner_points[(min_left, min_bot)] = 2 # 가장 바깥 사각형은 1번씩만 찍혔으므로 인위적으로 짝수로 변경
        inner_points[(min_left, max_top)] = 2
        inner_points[(max_right, min_bot)] = 2
        inner_points[(max_right, max_top)] = 2

        for i in inner_points.values():
            if i%2 != 0:
                return False
        return True
