# 기울기를 이용하여 같은 기울기 안에서 존재하는 최대 포인트 수를 구함
from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0 # 최종 최대 포인트 갯수 저장 변수 선언
        for p1 in points:
            slopes = defaultdict(int) # 한 포인트 마다 다른 포인트와의 기울기의 개수 카운팅하는 딕셔너리
            count = 0 # 한 기울기의 갯수 count
            max_num_points = 0
            for p2 in points:
                # 두 포인트가 같으면 다음 포인트로 바로 넘어감
                if p1 == p2:
                    continue
                    
                # 기울기 계산
                # 두 포인트 사이에 x값이 같으면 "inf"로 딕셔너리의 value를 저장
                if p2[0] != p1[0]:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                else:
                    slope = "inf"
                
                # slope의 갯수 카운트
                count = slopes[slope] + 1 
                slopes[slope] = count
                
                # p1에서 같은 기울기를 가지는 최대 point 갯수 갱신
                max_num_points = max(max_num_points, count)
                
            res = max(res, max_num_points+1) # 최종 최대 포인트 갯수 저장
        return res
