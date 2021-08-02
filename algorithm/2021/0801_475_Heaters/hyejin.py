class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 위치 정렬
        houses.sort()
        heaters.sort()
        max_radius = 0 # 가장 큰 radius
        curr_heat = 0 # 현재 heater 위치
        # 현재 house 위치에서 가장 가까운 heater를 curr로 설정
        for i in range(len(houses)):
            for heater_i in range(curr_heat, len(heaters)-1):
                if abs(houses[i] - heaters[heater_i]) < abs(houses[i] - heaters[heater_i+1]):
                    curr_heat = heater_i
                    break
                curr_heat = heater_i+1
            # 더 큰 radius를 선택해야함 (모든 위치에 만족하는 가장 작은 radius이어야하므로)
            max_radius = max(max_radius, abs(houses[i] - heaters[curr_heat]))
            
        return max_radius
