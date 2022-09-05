class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        # 꽃이 피기 시작하는 것과 지는 시간을 담을 리스트를 따로 선언
        start, end = [], []
        
        # 각 리스트에 해당 시간 인덱스 넣어주기
        for flower in flowers:
            start.append(flower[0])
            end.append(flower[1] + 1)
    
        # 시작과 끝 인덱스 정렬
        start.sort()
        end.sort()
        ans = []
        
        # 현재 person까지 핀 꽃과 진 꽃의 수를 구해서 빼기
        for person in persons:
            num_bloom = bisect.bisect_right(start, person)
            end_bloom = bisect.bisect_right(end, person)
            ans.append(num_bloom - end_bloom)
        
        return ans
