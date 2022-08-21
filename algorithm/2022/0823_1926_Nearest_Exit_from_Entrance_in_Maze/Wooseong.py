class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        
        # 위, 오른쪽, 아래, 왼쪽 반복문을 위한 리스트
        d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # 현재 위치(들)을 넣을 deque
        q = collections.deque()
        q.append((entrance[0], entrance[1]))
        # 방문 지점 탐색할 set
        visited = set()
        visited.add(tuple(entrance))
        
        # q가 빌 때까지: 더 이상 진행 가능한 위치가 없을 때까지
        distance = 0
        while q:
            # 일단 현재 있는 애들은 다 돌려야됨
            for _ in range(len(q)):
                r, c = q.popleft()
                # 위, 오른쪽, 아래, 왼쪽
                for dr, dc in d:                    
                    nr = r + dr
                    nc = c + dc
                    # 범위를 벗어나거나 탐색했거나 벽이면 끝
                    if ((not (0 <= nr < rows)) or (not (0 <= nc < cols)) or
                        ((nr, nc) in visited) or (maze[nr][nc] == '+')):
                        continue
                    # 끝에 다 왔으면: BFS니까 제일 빠를 때를 의미함 - return
                    if (nr in [0, rows - 1]) or (nc in [0, cols - 1]):
                        return distance + 1
                    
                    # 계속 진행
                    q.append((nr, nc))
                    visited.add((nr, nc))
            # for문을 다 돌았다 == 한 칸 움직이는 게 끝났다
            distance += 1
        
        # while을 다 돌아버렸다 == 진행 가능 한 게 없는데 return을 안 했다
        # == 불가능하다
        return -1
