# 2020.1.2
# baekjoon, 떡먹는 호랑이

tmp = input().split(" ")
D = int(tmp[0])
K = int(tmp[1])

fibo = [0,1,1]

for i in range(3, D+1) :
    fibo.append(fibo[i-1] + fibo[i-2])

a = fibo[D-2]
b = fibo[D-1]

temp = 0

while(True) :
    firstDay = temp
    temp += 1
    if (K-a*firstDay)%b :
        continue

    secondDay = int((K-a*firstDay)/b)

    if firstDay > secondDay :
        print(secondDay)
        print(firstDay)
    else:
        print(firstDay)
        print(secondDay)
    break
