from collections import defaultdict
from sys import maxsize
MAX_INT = maxsize
'''
time_limited... dp 써야할 듯
'''

class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        '''
        grid, moveCost -> Graph 구조로 변환
            - key: 출발지점, value: [도착지, cost]
        '''
        value_to_index = dict()
        '''
        value_to_index: 구조 변환을 위해 제작
        key: value, output: index
        e.g.
            문제에 제시된 Example 1 기준, 
            {5: [0, 0], 3: [0, 1], 4: [1, 0], 0: [1, 1], 2: [2, 0], 1: [2, 1]}
        '''
        for i, row_list in enumerate(grid):
            for j, val in enumerate(row_list):
                value_to_index[val] = [i,j]

        self.graph = defaultdict(list)
        for i, row_list in enumerate(moveCost):
            for j, cost in enumerate(row_list):
                # 출발지: value i를 가진 지점
                # 도착지: value i를 가진 지점의 row + 1, j
                # 이동비용: cost
                if value_to_index[i][0] == len(grid) - 1:
                    continue
                self.graph[grid[value_to_index[i][0]][value_to_index[i][1]]].append([grid[value_to_index[i][0] + 1][j], cost])
        '''
        self.graph 
        e.g.:
            {0: [[2, 9], [1, 8]], 3: [[4, 18], [0, 6]], 4: [[2, 2], [1, 4]], 5: [[4, 14], [0, 3]]}
        '''

        self.ans = MAX_INT
        self.dp = defaultdict(lambda: MAX_INT)  # 한 번 방문한 위치에 대하여 최솟값 저장

        for start in grid[0]:  # 첫번째 출발지 
            for second_start, cost in self.graph[start]:  # 두번째 출발지
                self.ans = min(self.ans, start+cost+self.dfs(second_start))  # 첫번째 출발지 + cost(첫번째 출발지 -> 두번쨰 출발지) + 이후 나올 수 있는 가장 최솟값

        return self.ans

    def dfs(self, pos):
        if self.dp[pos] != MAX_INT:  # 한 번 방문했던 위치라면 dp값 return
            return self.dp[pos]

        if len(self.graph[pos]) == 0:  # 마지막 위치라면
            return pos

        min_path = MAX_INT
        for next_pos, next_cost in self.graph[pos]:
            min_path = min(min_path, next_cost + pos + self.dfs(next_pos))  # 현재 위치에서 나올 수 있는 최소 경로 계산
        self.dp[pos] = min_path
        return self.dp[pos]  # 현재 위치에서 나올 수 있는 최소 경로 return
