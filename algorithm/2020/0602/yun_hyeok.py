PROBLEM_N = 11
problems_d_v = sorted([tuple(map(int, input().split())) for _ in range(PROBLEM_N)], key=lambda x: x[0])
total_penalty = 0
t = 0
for i in range(PROBLEM_N):
    d, v = problems_d_v[i]
    t += d
    total_penalty += t + 20*v
print(total_penalty)
