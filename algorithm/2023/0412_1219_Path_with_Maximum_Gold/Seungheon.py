# fail code
# dp로풀어보려했지만 실패 이렇게 풀면 안되는둣


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        # 시작위치부터 최대값찾기
        # dp
        def initialize(i, j):
            visited = [[0 for _ in grid[0]] for _ in grid]
            tmp_gird = copy.deepcopy(grid)
            max_gold = 0
            def explore(i, j, prv_g = 0):
                nonlocal max_gold
                
                # for asd in tmp_gird:
                #     print(asd)
                # print()
                # 범위밖 처리
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                    return

                # 방문체크
                if visited[i][j] == 1:
                    return
                visited[i][j] = 1

                # 금이 없으면 안감
                if tmp_gird[i][j] == 0:
                    return

                tmp_gird[i][j] += prv_g
                tmp_gold = tmp_gird[i][j]

                max_gold = max(max_gold, tmp_gird[i][j])

                for di, dj in ([1,0],[0,1],[-1,0],[0,-1]):
                    explore(i+di,j+dj, tmp_gold)

            explore(i, j)

            return max_gold 

        answer = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                answer = max(answer, initialize(r,c))

        return answer
        
