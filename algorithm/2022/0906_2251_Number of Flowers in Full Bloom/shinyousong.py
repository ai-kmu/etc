# 개화 시기가 되면 (기준이 꽃이 지는 시기인) 힙에 넣는다
# "시간 범위"에 따른 꽃 개화 데이터를 만든다.
# "시간 범위"에 따라서 결과를 낸다.
# 시간초과(아마 무한루프 해결 실패?)
import heapq
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        # 개화 시기 정렬과 타임 인덱스
        flowers.sort(key = lambda x: x[0], reverse = True)
        t = 1
        t_sec = 1
        # 꽃이 지는 시기 힙
        died = []
        # 시간 범위 개화 데이터
        data = []
        while flowers or died:
            # 현재로부터 가장 피는 꽃으로부터 개화날과 지는날을 가져온다.
            if flowers:
                flower = flowers.pop()
                t = flower[0]
                die = flower[1]
                heapq.heappush(died, die)
            # 같은 날짜면 전부 가져온다
            while flowers and flowers[-1][0] == t:
                flower = flowers.pop()
                die = flower[1]
                heapq.heappush(died, die)
            # 그 날짜까지 갱신한다.
            while t_sec < t:
                if died[0] < t:
                    data.append([died[0], len(died)])
                    t_sec = died[0]
                    heapq.heappop(died)
                else:
                    t_sec = t
                    
        # 이제 결과를 낸다.
        res = []
        for person in persons:
            i = 0
            while person <= died[i][0]:
                i += 1
                tmp = died[i][1]
            res.append
        return res
                
            
