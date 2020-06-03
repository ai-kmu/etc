import sys
# greedy 알고리즘

# (한 문제당 걸리는 시간, verdict) 튜플을 list에 저장
problem_times = []

for i in range(11):
    time, verdict = map(int, sys.stdin.readline().rstrip().split())
    problem_times.append((time,verdict))


# time이 빠른 순으로 정렬
problem_times = sorted(problem_times, key=lambda x: x[0])

# time: 문제 풀었을 때 누적 시간
# total_panelty : 전체 패널티
total_panelty = 0
time = 0

# for문 돌면서 패널티 추가
for i in range(11):
    time += problem_times[i][0]
    total_panelty += time + problem_times[i][1]* 20

print(total_panelty)
