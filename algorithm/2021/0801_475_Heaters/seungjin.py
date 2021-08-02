from bisect import bisect_left , bisect_right #이진탐색 모듈
def findRadius(houses , heaters):
    houses.sort()
    heaters.sort()
    min_len = []
    for house in houses:
        index = bisect_left(heaters , house) #index 반환

        if 0<index<len(heaters): #양 옆의 히터중 가까운 곳을 반환한다.
            min_len.append(min(abs(house - heaters[index-1]), abs(heaters[index] - house)))
        else: #heater의 배열 끝자리에 위치할 경우 
            min_len.append(heaters[0] - house if index ==0 else house - heaters[-1] )
    return max(min_len)
