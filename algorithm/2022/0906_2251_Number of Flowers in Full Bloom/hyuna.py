class Solution(object):
    def fullBloomFlowers(self, flowers, persons):
        """
        :type flowers: List[List[int]]
        :type persons: List[int]
        :rtype: List[int]
        """
        '''
        for문을 여러번 돌렸을 때 시간 초과가 나기 때문에 바이너리 서치를 사용함
        각 사람마다 도착한 시간에 따라 꽃이 핀 개수에서 진 개수를 빼개되면 해당 시간에 피어있는 꽃의 개수를 계산 할 수 있음
        '''
        
        bloom = []
        # 이진 탐색을 위해 꽃이 핀 시간과 진 시간을 각각 리스트에 넣고 정렬해준다
        start = sorted([flower[0] for flower in flowers])
        end = sorted([flower[1] for flower in flowers])
        
        # 꽃이 핀 시간 탐색을 위한 함수
        def searchStart(time):
            low = 0
            high = len(start)
            while low < high:
                # 리스트의 중간 값을 찾기 위해 low high를 더하고 2로 나눠준다
                mid = (low + high) // 2
                # start 리스트의 중간 값(꽃이 피기 시작한 값들 중 하나)이 사람이 도착한 시간의 값보다 작거나 같으면 
                # low값을 바꿔주고 아닐경우 high의 값을 바꿔준다
                if start[mid] <= time:
                    low = mid + 1
                else:
                    high = mid 
            
            return high
        
        # 꽃이 진 시간 탐색을 위한 함수
        def searchEnd(time):
            low = 0
            high = len(end)
            while low < high:
                mid = (low + high) // 2
                # end 리스트의 중간 값(꽃이 진 시기의 값들 중 하나)이 사람이 도착한 시간의 값보다 작으면 
                # low값을 바꿔주고 아닐경우 high의 값을 바꿔준다
                if end[mid] < time:
                    low = mid + 1
                else:
                    high = mid 
            
            return high
        
        for person in persons:
            # 답변 리스트에 해당 시점에 펴있는 꽃의 개수 (해당 시점에 피어있는 꽃 - 해당 시점에 져있는 꽃)를 append시킨다
            bloom.append(searchStart(person) - searchEnd(person))
            
        return bloom
