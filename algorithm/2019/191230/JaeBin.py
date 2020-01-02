# 2. 떡 먹는 호랑이

d, cnt = input().split()
day = int(d)
count = int(cnt)

ddeok = []
for i in range(31):
    ddeok.append(0)

ddeok[1] = 1
ddeok[2] = 1

for i in range(3, day+1):
    ddeok[i] = ddeok[i-1] + ddeok[i-2]

front = ddeok[day-2]
rear = ddeok[day-1]

est = 1
while True:
    first = est
    est += 1
    first = est
    if (count - front * first) % rear:
        continue
    else:
        second = int((count - front * first) / rear)
        break

print(first)
print(second)