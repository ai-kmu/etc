penalty = 0               # 총 패널티
cumulative_time = 0       # 문제 푸는데 걸리는 시간을 누적해서 더할 변수
scores = []               # 각 문제를 푸는데 걸리는 시간과 incorrect verdicts를 이중리스트로 저장할 리스트


#입력받는 부분
for i in range(11):
    D, V = map(int, input().split())
    scores.append([D,V])

# 오름차 순으로 정렬해서 시간이 적게 걸리는 문제부터 
scores.sort()

# 더해주기
for i,j in scores:
    penalty += i + cumulative_time + j*20
    cumulative_time += i


print(penalty)
