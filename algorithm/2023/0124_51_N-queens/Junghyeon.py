'''
backtracking + dfs로 풀이
'''
class Solution(object):
    def solveNQueens(self, n):
        def dfs(n, col, temp, ans):
            if len(temp) == n:
                ans.append(temp[:])
            for i in range(n):
                if not any([col - x == 0 or i - y == 0 or abs(col - x) == abs(i - y) for x, y in temp]):
                    temp.append((col, i))
                    dfs(n, col + 1, temp, ans)
                    temp.pop()

        locations = []
        # dfs 탐색
        dfs(n, 0, [], locations)

        ans = []
        for i in range(len(locations)):
            l = [['.'] * n for _ in range(n)]
            for col, row in locations[i]:
                l[col][row] = 'Q'
            ans.append(l)
            
        return [[''.join(row) for row in one] for one in ans]
