# 140 테케에서 실패..

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # 유효거리 정의
        is_in = lambda a, b: (a[0] - b[0])**2 + (a[1] - b[1])**2 <= a[2]**2

        # 유효거리 이내 폭탄 리스트
        booms = [[j for j in range(len(bombs)) if (j != i and is_in(bombs[i], bombs[j]))] for i in range(len(bombs))]

        print(booms)

        ret = 0

        # i번째 index에서 폭탄 계산
        def bfs(v, i):
            queue = booms[i]
            v[i] = 1

            while queue:
                print(queue)
                j = queue.pop()
                if v[j]:
                    continue

                queue += booms[j]
                v[j] = 1

            print(f"i total : {v}")

        # 계산
        for i in range(len(bombs)):
            print(i, "="*10)
            visited = [0 for i in range(len(bombs))]
            bfs(visited, i)

            print(sum(visited))

            ret = max(ret, sum(visited))

        return ret

        




    

        

