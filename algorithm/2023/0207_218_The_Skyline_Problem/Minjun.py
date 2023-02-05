class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        start_x, end_x = buildings[0][0], buildings[0][1]
        height = buildings[0][2]
        skyline = [[start_x, height]]
        for i,j,y in buildings:
            # 현재 건물이 이전 건물보다 짧으면,
            if end_x < j:
                # 심지어 높이도 짧으면,
                if height >= y:
                    pass
                # 높이가 크면
                else:
                    skyline.append([i, y])
                    skyline.append([j, end_x])
        print(skyline)
