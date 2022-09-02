from bisect import bisect_right
from collections import defaultdict


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        flower_dict = defaultdict(int)
        
        # 시작점과 끝점을 각각 정렬
        starts = sorted([x[0] for x in flowers])
        # 끝점 다음부터 꽃의 개수가 하나 감소하므로
        # x[1]이 아닌 x[1]+1로 설정
        ends = sorted([x[1]+1 for x in flowers])
        
        start_cursor, end_cursor = 0, 0
        n = len(flowers)
        
        # 꽃의 개수를 저장해가며
        # 시작점을 만날 경우 꽃의 개수를 +1,
        # 끝점을 만날 경우 꽃의 개수를 -1한 다음
        # 해당 위치에서의 꽃의 개수를 저장한다.
        count = 0
        all_points = []
        while start_cursor < n or end_cursor < n:
            start = starts[start_cursor] if start_cursor < n else float('inf')
            end = ends[end_cursor] if end_cursor < n else float('inf')
            if start < end:
                count += 1
                flower_dict[start] = count
                start_cursor += 1
            else:
                count -= 1
                flower_dict[end] = count
                end_cursor += 1
        
        all_points = sorted(flower_dict.keys())
        # person의 위치가 주어졌을 때
        # bisect를 활용하여 바로 왼쪽에 있는 점을 찾아 해당 점에서의 꽃의 개수를 리턴한다.
        return list(map(lambda person: flower_dict[all_points[bisect_right(all_points, person)-1]], persons))
