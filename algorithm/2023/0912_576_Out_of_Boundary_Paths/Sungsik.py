class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # table을 row랑 column을 상하좌우로 늘려서 모서리에 도달한 횟수를 계산하는 방식으로 구함
        table = [[0] * (n+2) for _ in range(m+2)]
        table[startRow+1][startColumn+1] = 1

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for move in range(maxMove):
            new_table = [row.copy() for row in table]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    # 현재 위치에 도달한 횟수를 상하좌우로 전달
                    if table[i][j]:
                        for di, dj in dirs:
                            new_i, new_j = i + di, j + dj
                            new_table[new_i][new_j] += table[i][j]
                        # 현재 위치의 횟수는 0이 됨
                        new_table[i][j] = 0
            table = new_table
            
        answer = 0
        answer += sum(table[0]) + sum(table[-1])
        for i in range(1, m+1):
            answer += table[i][0] + table[i][-1]
        
        return answer % (10 ** 9 + 7)
