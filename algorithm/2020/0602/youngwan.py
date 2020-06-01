import sys


solve_time_list = []                      # 문제 풀이 시간 저장
penalty = 0                               # penalty 개수 저장
for line in sys.stdin.readlines():
    line = line.split()
    solve_time_list.append(int(line[0]))
    penalty += int(line[1])

penalty *= 20                             # penalty 개수 * 20
solve_time_list.sort()                    # 풀이 시간이 짧은 순으로 저장
total_time = 0                           
for time in solve_time_list:              
    total_time += time                    # 시간을 계속 더하고
    penalty += total_time                 # penalty에 더해준다

print(penalty)
