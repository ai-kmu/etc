class Solution(object):
    def findRadius(self, houses, heaters):
        houses.sort() ## 오름차순 순서대로 정렬
        heaters.sort() ## 오름차순 순서대로 정렬
        dp = [] ## 거리 후보
        ## 집마다 가장 가까운 난방기와의 위치를 구하기 
        for house in houses:
            idx = bisect.bisect_left(heaters, house) ## 오름차순을 유지하면서 히터 위치에 들어 갈 수 있는 집 idx 찾기
            if idx == 0: ## 0이면 집 위치가 히터[0] 위치의 왼쪽에 있다는 것을 의미
                # house is in the left of heaters
                dp.append(heaters[0] - house)
            elif idx == len(heaters): ## len(heaters)이면 집 위치가 히터[-1] 위치의 오른쪽에 있다는 것을 의미
                # house is in the right of heaters
                dp.append(house - heaters[-1])
            else: ## 위 경우에 해당되지 않으면 히터 위치가 집 사이에 있다는 것을 의미
                # get the min distance between two heaters
                dp.append(min(house - heaters[idx-1], heaters[idx]-house)) ## 히터의 왼쪽 집과의 거리와 히터의 오른쪽 집과의 거리를 구해서 판단
                
        return max(dp)
