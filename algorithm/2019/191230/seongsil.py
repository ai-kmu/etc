def solution(day, num):

    d = [[1,0],[0,1]]

    while True:
        if len(d) == day:
            break
        d.append([d[-1][0] + d[-2][0], d[-1][1] + d[-2][1]])
    y = 1

    answer = False
    
    while True:
        x = 1
        while x <= y:
            if (d[-1][0]*x + d[-1][1]*y) == num:
                print(x)
                print(y)
                answer = True
                break
            x += 1
        
        y += 1
        if answer is True:
            break

day, num = map(int, input().split())

solution(day, num)
