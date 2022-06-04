class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def fall(grid_map, r, c):
            if c <= len(grid_map[0])-2 and c >= 1: # 현재 dfs 함수 안에서 grid 열 인덱스가 '0 < grid 열 인덱스 < (grid의 열 길이-1)' 인 경우
                if grid_map[r][c] == grid_map[r][c+1] and grid_map[r][c] == 1: # 오른쪽 아래 방향 대각선으로 공이 흘러갈 수 있는 경우
                    # 마지막 row이면 열 인덱스+1 값 리턴
                    # 마지막 row가 아니면 dfs 반복
                    if r == len(grid_map)-1:
                        return c+1
                    else:
                        return fall(grid_map,r+1,c+1)
                elif grid_map[r][c] == grid_map[r][c-1] and grid_map[r][c] == -1: # 왼쪽 아래 방향 대각선으로 공이 흘러갈 수 있는 경우
                    # 마지막 row이면 열 인덱스-11 값 리턴
                    # 마지막 row가 아니면 dfs 반복
                    if r == len(grid_map)-1:
                        return c-1
                    else:
                        return fall(grid_map,r+1,c-1)
                elif grid_map[r][c] != grid_map[r][c+1] or grid_map[r][c] != grid_map[r][c-1]: # V 모양에 갇힌 경우 -1 리턴
                    return -1
            else:
                if c == 0: # grid 인덱스가 0인 경우
                    # grid 열 개수가 2개 이상이면 grid 값이 -1이거나 V자로 갇힌경우는 -1 리턴
                    # 그 외에는 밑으로 흘러갈 수 있으므로 이때 마지막 row이면 최종 열에서 1 더한 값 리턴
                    # 마지막 row가 아니면 dfs 반복
                    if len(grid_map[0]) != 1:
                        if (grid_map[r][c] == -1) or (grid_map[r][c] != grid_map[r][c+1]):
                            return -1
                        else:
                            if r == len(grid_map)-1:
                                return c+1
                            else:
                                return fall(grid_map,r+1,c+1)
                    # 열 개수가 하나인 경우는 무조건 갇히므로 -1 리턴
                    else:
                        return -1
                elif c == len(grid_map[0])-1: # grid 인덱스가 열 끝인 경우
                    # grid 값이 1이거나 V자 모양으로 갇힌 경우 -1 리턴
                    # 그 외에는 밑으로 흘러갈 수 있으므로 이 때 마지막 row이면 최종 열에서 1 뺀 값 리턴
                    # 마지막 row가 아니면 dfs 반복
                    if (grid_map[r][c] == 1) or (grid_map[r][c] != grid_map[r][c-1]):
                        return -1
                    else:
                        if r == len(grid_map)-1:
                            return c-1
                        else:
                            return fall(grid_map,r+1,c-1)
            
        ans = []
        for i in range(len(grid[0])):
            answer = fall(grid,0,i)
            ans.append(answer)
        return ans
