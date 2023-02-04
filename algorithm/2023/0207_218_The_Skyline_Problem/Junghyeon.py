'''
조건이 다양해서 여러 조건을 고려하며 풀어보았지만 실패...
23 / 41 testcases passed
'''
class Solution(object):
    def getSkyline(self, buildings):
        new_buildings = [buildings[0]]

        # 다른 건물에 완전히 가려지는 건물은 제거
        for i in range(1, len(buildings)):
            prev_l = new_buildings[-1][0] 
            prev_r = new_buildings[-1][1]
            prev_h = new_buildings[-1][2]
            
            curr_l = buildings[i][0]
            curr_r = buildings[i][1]
            curr_h = buildings[i][2]
            
            if prev_l == curr_l and prev_r <= curr_r and prev_h < curr_h:
                new_buildings[-1] = [curr_l, curr_r,  curr_h]
                continue
            if curr_r <= prev_r and curr_h < prev_h:
                continue
            else:
                new_buildings.append([curr_l, curr_r,  curr_h])

        buildings = new_buildings[:]

        last = sorted(buildings, key = lambda x: (x[1], x[2]))[-1]
        first = sorted(buildings, key = lambda x: (x[0], -x[2]))[0]

        result = []
        result.append([first[0], first[2]])

        # 왼쪽 정보를 기준으로 정렬
        buildings.sort()

        for i in range(len(buildings)-1):
            prev_l = buildings[i][0] 
            prev_r = buildings[i][1]
            prev_h = buildings[i][2]
            
            curr_l = buildings[i+1][0]
            curr_r = buildings[i+1][1]
            curr_h = buildings[i+1][2]
            
            # horizontal segment -> height가 같은지에 따라 결정
            if prev_h != curr_h and curr_l <= prev_r:
                if prev_h < curr_h:
                    result.append([curr_l, curr_h])
                else:
                    result.append([prev_r, curr_h])
            
            # height가 같아도 건물이 아예 중첩되지 않은 경우에는 horizontal segment가 생김
            else:
                if prev_r < curr_l:
                    result.append([prev_r, 0])
                    result.append([curr_l, curr_h])

        result.append([last[1], 0])

        return result
