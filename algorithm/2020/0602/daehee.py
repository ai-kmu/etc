# 1. D, V 리스트 저장하기
DV = list()
for _ in range(11):
    d,v  = map(int, input().split())
    DV.append([d,v])    

# 2. DV 리스트 오름차순 정렬
DV.sort()

# 3. V 누적시키며 적게 걸리는 것부터 계산하기
answer = 0
V = 0
for dv in DV:
    answer += dv[0] + V + 20*dv[1]
    V += dv[0]

print(answer)
