D, K = map(int, input().split())

days = [[0,0]]
days.append([1,0])
days.append([0,1])

for day in range(3,D+1):
    days.append([days[day-1][0] + days[day-2][0],days[day-1][1] + days[day-2][1]])

condition = False
y = 1
x = 1

while y*days[D][1]<=K:
    x = 1
    while x<= y:
        if (days[D][0]*x + days[D][1]*y) == K:
            print(x)
            print(y)
            condition = True
            break
        x += 1
    if condition is True:
        break
    y += 1