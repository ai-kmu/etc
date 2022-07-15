import sys

m = int(input())

graph = []

for i in range(m):
    graph.append(list(input()))

n = len(graph[0])

def dfs(graph, i, j):

    if i < 0 or i >= m or j < 0 or j >= n:
        return 0
    if graph[i][j] == '0':
        return 0
    if graph[i][j] == '1':
        graph[i][j] = '0'

        return 1 + dfs(graph, i-1, j) + dfs(graph, i+1, j) + dfs(graph, i, j-1) + dfs(graph, i, j+1)


answer = []
nums = 0
for i in range(m):
    for j in range(n):
        val = dfs(graph, i, j)
        if val != 0:
            nums += 1
            answer.append(val) 

print(nums)
answer.sort()
for i in answer:
    print(i)
