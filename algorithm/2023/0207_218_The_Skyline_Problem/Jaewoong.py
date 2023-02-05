# 풀이실패...
# 풀이방법봤는데 어려워서 포기했읍니다...
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        point_l = []
        for l,r,h in buildings:
            point_l.append([l,h])
            point_l.append([l,h-1])
            if h == 0:
                break

        point_r = []
        for l,r,h in buildings:
            point_r.append([r,h])
            point_r.append([r,h-1])

        answer = []
        for i in point_l:
            for j in point_r:
                if i in j:
                    answer.append(i)

        return answer
