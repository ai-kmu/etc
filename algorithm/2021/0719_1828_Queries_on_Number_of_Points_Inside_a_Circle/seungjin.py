class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        circle_map = []
        for circle in queries:
            circle_map.append(0)
            for point in points:
                if (circle[0]-point[0])*(circle[0]-point[0]) + \
                (circle[1]-point[1])*(circle[1]-point[1]) <= circle[2]*circle[2]:
                    circle_map[-1] += 1
        return circle_map
