#너비 우선 탐색(BFS, Breadth-First Search)문제

import sys
# sys.stdin = open("input.txt", 'r')

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def bfs(v):
    
    q = [v]
    level = 0
    state = False
    
    while q:
        level += 1
        for _ in range(len(q)):
            v = q.pop(0)
            
            if v == (row, col):
                state = True
                break
                
            if maze[v[0]][v[1]] == '1':
                    maze[v[0]][v[1]] = '0'
                    for i in range(len(move)):
                        if maze[v[0]+move[i][0]][v[1]+move[i][1]] == '1':
                            q.append((v[0]+move[i][0], v[1]+move[i][1]))
        if state:
            break
    return level


if __name__ == "__main__":
    row, col = map(int, input().split())
    maze = [['0'] * (col + 2)] + [list('0' + input() + '0') for _ in range(row)] + [['0'] * (col + 2)]
    print(bfs((1,1)))
