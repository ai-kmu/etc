cases=int(input())

#2차원 배열 만들어서 0으로 초기화
grid=[]
for i in range(101):
    array=[0 for i in range(101)]
    grid.append(array)

#각 색종이 영역에 각 index 넣어줌
for i in range(1,cases+1):
    xPoint,yPoint, width, height=map(int,input().split())

    #세로로 먼저 지나가고 가로 움직임
    #가로(열)
    for m in range(xPoint, xPoint+width):
        #세로(행)
        for n in range(yPoint,yPoint+height):
            grid[m][n]=i

#숫자 세기
for i in range(1,cases+1):
    count=0

    #가로(열)
    for j in range(101):
        #세로(행)
        for m in range(101):
            if grid[j][m]==i:
                count+=1
    print(count)




