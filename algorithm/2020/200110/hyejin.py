count = int(input())
line_list = []

for i in range(count):
    fir, sec = map(int, input().split())
    line_list.append([fir, sec])

# 시작점의 좌표 순서대로 정렬
sorted(line_list, key=lambda first: line_list[0])

before_fir = line_list[0][0]
before_sec = line_list[0][1]
answer = before_sec - before_fir

for fir, sec in line_list:
    # 현재 sec가 이전 sec보다 작다면 넘어감.
    if sec <= before_sec:
        continue
    # 현재 fir가 전 sec보다 작거나 같다면, answer += 현재 sec- 전 sec
    elif fir <= before_sec:
        answer += sec - before_sec
        before_sec = sec
    # 현재 fir가 전 sec보다 크다면, answer += 현재 sec - 현재 fir
    else:
        answer += sec - fir
        before_fir = fir
        before_sec = sec

print(answer)