class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # 거리 계산 : 6가지, 변 4개 대각선 2개
        # 정사각형 : 네변 길이 같고 대각선 길이도 같음
        def distance(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2

        dists = [distance(p1, p2), distance(p1, p3), distance(p1, p4), distance(p2, p3), distance(p2, p4), distance(p3, p4)]
        dists.sort() # 마지막 두개가 정사각형 기준 대각선

        # 변의 길이는 대각선이랑 같으면 안되어 예외 처리
        return (dists[0] == dists[1] == dists[2] == dists[3] != dists[4]) and (dists[4] == dists[5])
        
