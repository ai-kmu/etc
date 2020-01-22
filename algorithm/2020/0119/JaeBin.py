# 4. 네트워크

def solution(n, computers):
    answer = 0
    bfs = []
    visited = [0] * n

    while 0 in visited:
        x = visited.index(0)
        bfs.append(x)
        visited[x] = 1

        while bfs:
            first = bfs.pop(0)
            visited[first] = 1

            for i in range(n):
                if visited[i] == 0 and computers[first][i] == 1:
                    bfs.append(i)
                    visited[i] = 1
        answer += 1
    return answer

# input_n_1 = 3
# input_computers_1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# print(solution(input_n_1, input_computers_1))
# print()
# input_n_2 = 3
# input_computers_2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
# print(solution(input_n_2, input_computers_2))