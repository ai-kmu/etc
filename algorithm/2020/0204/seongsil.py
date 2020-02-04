n = int(input())
MAX = 101

papers = [[0 for i in range(MAX)] for j in range(MAX)]
for num in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x + w):
        for j in range(y, y+h):
            papers[i][j] = num
            
for i in range(1, n+1):
    area = 0
    for j in range(MAX):
        for k in range(MAX):
            if first[j][k] == i:
                area += 1
                
    print(area)
