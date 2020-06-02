import sys


time = list()
penalty = list()
for data in sys.stdin.readlines():
    data = data.split()
    time.append(int(data[0]))
    penalty.append(int(data[1]))
    
answer = sum(penalty) * 20  # 패널티 총합 *20
time.sort()
accumulate_time = 0
for t in time:
    accumulate_time += t #문제푸는데 걸린시간 누적
    answer += accumulate_time
    
print(answer)
