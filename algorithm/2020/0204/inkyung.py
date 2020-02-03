n = int(input())

#101 * 101 의 그리드를 생성
first = [[0 for i in range(101)] for j in range(101)]

#input 값을 각각 x, y, width, height으로 저장하고
#시작점인 x, y에서 width와 height만큼 반복하면서 그 부분에 몇 번째
#색종이가 겹쳐져 있는지 표시함
for num in range(1, n + 1):
    x, y, width, height = map(int, input().split())
    for i in range(x, x + width):
        for j in range(y, y + height):
            first[i][j] = num

#n개의 색종이의 면적을 찾기 위해서
#반복하면서 n번째 색종이로 표현된 부분을 찾고 해당 부분을 count해서 print
for i in range(1, n + 1):
    count = 0
    for j in range(101):
        for k in range(101):
            if first[j][k] == i:
                count += 1
    print(count)
