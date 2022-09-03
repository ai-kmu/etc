from bisect import bisect_left, bisect_right

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        
        answer = []
        
        # 시작하는 부분을 기준으로 정렬
        start_sorted_flowers = [s[0] for s in sorted(flowers, key = lambda x : x[0])]
        # 끝나는 부분을 기준으로 정렬
        end_sorted_flowers = [e[1] for e in sorted(flowers, key = lambda x : x[1])]

        # person의 위치를 기준으로 앞에 시작하는부분과 끝나는부분의 차이로 꽃의 개수를 구함
        # 꽃이 시작하는 개수 - 꽃이 끝나는 개수 = person이 볼 수 있는 꽃의 개수
        for p in persons:
            
            # person 앞에 꽃이 시작하는 부분의 개수(같은위치라면 꽃을 포함)
            a = bisect_right(start_sorted_flowers, p)
            # person 앞에 꽃이 끝나는 부분의 개수(같은위치라면 꽃을 포함하지 않음)
            b = bisect_left(end_sorted_flowers, p)
            
            answer.append(a - b)
        
        return answer
