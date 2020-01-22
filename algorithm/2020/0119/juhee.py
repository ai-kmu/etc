CONNECTED = 1;
DISCONNECTED = 0;


def solution(n, computers):
    answer = 2
    for i in range(n):
        for j in range(n):
            if computers[i][j] == CONNECTED:
                answer += 1
                computers[i][j] = answer
                q = []
                q.append(j)
                while len(q) != 0:
                    f = q.pop(0)
                    for i in range(n):
                        if computers[f][i] == CONNECTED:
                            computers[f][i] = answer
                            q.append(i)

    return answer - 2
