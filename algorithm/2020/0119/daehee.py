def dfs(start, computers, explored, n):
    explored.append(start)
    for i in range(n):
        if i not in explored and computers[start][i] == 1:
            dfs(i,computers,explored, n)

            
def solution(n, computers):
    answer = 0
    explored = list()
    
    for i in range(n):
        if i not in explored:
            answer += 1
            dfs(i, computers,explored, n)
            
    return answer
