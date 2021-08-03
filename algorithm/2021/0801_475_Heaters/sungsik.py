class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # list에서 num의 위치와 가까운 index를 출력하는 함수
        def binarySearch(num, array):
            minIdx = 0
            maxIdx = len(array) - 1
            while minIdx <= maxIdx: 
                midIdx = (minIdx + maxIdx) // 2 
                if array[midIdx] < num:
                    minIdx = midIdx + 1 
                else:
                    maxIdx = midIdx - 1 
            return minIdx

        # 이진 검색을 위해 heater를 정렬
        heaters.sort()
        answer = []
        for house in houses:
            # house마다 가장 가까운 heater의 index를 찾음 
            index = binarySearch(house, heaters)
            # 만약 처음과 마지막 heater가 가장 가깝다면 단순히 house와 해당 heater와의 차이를 추가한다.
            if index == 0:
                answer.append(heaters[0] - house)
            elif index == len(heaters):
                answer.append(house - heaters[-1])
            # 그렇지 않을 경우 house는 앞뒤 heater와의 차이중 작은 값을 추가한다.
            else:
                answer.append(min(heaters[index] - house, house - heaters[index-1]))
        return max(answer)
