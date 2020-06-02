# 22. 백준 - And the Winner Is ... Ourselves!

# 11개의 input줄 저장하는 lines
lines = 11

# 문제 푸는 시간 저장하는 list
time_lst = []

# 벌칙값 저장 변수
penalty = 0

# 11번 반복하면서 시간과 벌칙값 받는다
for t in range(lines):
    # 문제 푼 시간과 못 푼 문제 개수 받아오기
    D_i, V_i = map(int, input().split())
    # 리스트에 푼 시간 추가
    time_lst.append(D_i)
    # 못 푼 문제만큼 벌칙에 추가
    penalty += V_i


penalty *= 20
# 시간 순서대로 정렬
time_lst.sort()

total_time = 0

for time in time_lst:
    total_time += time
    penalty += total_time

print(penalty)


