# 2020.1.16
# baekjoon, 선긋기

def solution() :

    list = []
    n = int(input())
    for i in range(n) :
        list.append((input().split(" ")))

    list.sort()
    listLen = len(list)

    sum = 0
    sum += int(list[0][1]) - int(list[0][0])

    for i in range(1, listLen):
        if int(list[i-1][1]) > int(list[i][0]) :
            sum += int(list[i][1]) - int(list[i-1][1])
        else :
            sum += int(list[i][1]) - int(list[i][0])

    print(sum)


solution()
