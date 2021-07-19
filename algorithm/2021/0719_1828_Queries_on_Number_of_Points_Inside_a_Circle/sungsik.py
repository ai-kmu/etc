class Solution:
    # 거리의 제곱을 구하는 함수
    def calcSquaredDist(self, point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2
    
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = [0 for _ in range(len(queries))]
        for i, query in enumerate(queries):
            # 제곱을 비교하기 때문에 반지름도 제곱해준다
            squaredRadius = query[2] ** 2
            for point in points:
                # 점과 원의 중심과의 거리의 제곱이 반지름의 제곱보다 작을 경우 원의 내부에 있음
                if self.calcSquaredDist(point, query[:2]) <= squaredRadius:
                    answer[i] += 1
        
        return answer
