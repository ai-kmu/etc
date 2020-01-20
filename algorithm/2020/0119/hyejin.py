def solution(n, computers):
    answer = 0
    network = n
    visit = [0 for i in range(n)]

    def dfs(visit, r):
        stack = [r]
        while len(stack) != 0:
            r = stack.pop()
            visit[r] = 1
            for c in range(0, n):
                if computers[r][c] == 1 and visit[c] == 0:
                    stack.append(c)

    for i in range(n):
        if visit[i] == 0:
            dfs(visit, i)
            answer += 1

    # for i in range(n) :
    #     visit[i] =1
    #     for j in range(i,n) :
    #         if computers[i][j] == 1 and visit[j] ==0:
    #             network -= 1
    #             visit[j] = 1
    #         else :
    #             pass
    # answer = network

    return answer