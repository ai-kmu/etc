class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        
        # 시작 지점을 기준으로 정렬
        start = sorted([flower[0] for flower in flowers])
        # 종료 지점을 기준으로 정렬
        end = sorted([flower[1] for flower in flowers])
        answer = []
        
        for person in persons:
            s = bisect_right(start, person)
            e = bisect_left(end, person)
            
            # 두 index의 차이가 현재 person이 볼 수 있는 꽃의 개수가 된다
            answer.append(s-e)
            
        return answer
