from bisect import bisect_left, bisect_right
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        answer = []
        # 꽃이 피는 각각의 시간을 정렬해서 flowers_s에 저장
        flowers_s = [i for i, j in sorted(flowers)]
        # 꽃이 지는 각각의 시간을 정렬해서 flowers_e에 저장
        flowers_e = [j for i, j in sorted(flowers, key = lambda x: x[1])]
        # 사람이 온 시점에 꽃의 개수 = 사람이 온 시점에 꽃이 핀 개수(인덱스) - 사람이 온 시점에 꽃이 진 개수(인덱스)
        # 이 때 bisect를 이용하는데, 사람이 온 시점에 꽃이 핀 개수는 그 시점의 인덱스보다 오른쪽에서 찾아야 하므로 bisect_right로 구함
        for person in persons:
            answer.append(bisect_right(flowers_s, person) - bisect_left(flowers_e, person))
        return answer
