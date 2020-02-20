MAX = 999999


def bfs(current, target):
    distance = [MAX for i in range(100001)]
    q = []

    q.append((current, 0, 0))
    size = 1                    # 시간초과 방지를 위한 trick
    while size > 0:

        node = q[0]
        q = q[1:]
        size -= 1
        if node[0] == target :
            return distance[target]

        if node[0] > 0:
            if distance[node[0] - 1] > node[2] + 1:
                distance[node[0] - 1] = node[2] + 1
                q.append((node[0] - 1, 2, node[2] + 1))
                size += 1

        if node[0] < 100000:
            if distance[node[0] + 1] > node[2] + 1:
                distance[node[0] + 1] = node[2] + 1
                q.append((node[0] + 1, 2, node[2] + 1))
                size += 1
        if node[0] * 2 <= 100000:
            if distance[node[0] * 2] > node[2]:
                distance[node[0] * 2] = node[2]
                q.append((node[0] * 2, 3, node[2]))
                size += 1


def main():
    inp = input().split(" ")

    N = int(inp[0]);
    K = int(inp[1])

    if N == K or N * 2 == K:
        print(0)

    elif K < N:
        print(N - K)

    else:
        print(bfs(N, K))

main()
