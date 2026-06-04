class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # 유효거리 정의 방정식
        is_in = lambda a, b: (a[0] - b[0])**2 + (a[1] - b[1])**2 <= a[2]**2

        # 유효거리 이내 폭탄 리스트
        booms = [[j for j in range(len(bombs)) if (j != i and is_in(bombs[i], bombs[j]))] for i in range(len(bombs))]

        ret = 0

        # i번째 index에서 폭탄 계산
        for i in range(len(bombs)):
            visited = [0 for i in range(len(bombs))]
            queue = booms[i][::]
            visited[i] = 1

            #bfs
            while queue:
                j = queue.pop()

                if visited[j]:
                    continue

                visited[j] = 1
                queue += booms[j]

            ret = max(ret, sum(visited))

        return ret
