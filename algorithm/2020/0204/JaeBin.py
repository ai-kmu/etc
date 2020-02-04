# 6. 색종이

count = int(input())
plane = [[0 for i in range(101)] for j in range(101)]
cnt = [0] * 101

for i in range(1, count+1):
    x, y, width, height = map(int, input().split())
    for j in range(x, x+width):
        for k in range(y, y+height):
            plane[j][k] = i

for i in range(101):
    for j in range(101):
        cnt[plane[i][j]] += 1

for i in range(1, count+1):
    print(cnt[i])
