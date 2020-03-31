N, K = map(int, input().split())
value = []  # 우리가 가지고 있는 동전 값들을 담을 리스트
num = 0     # 우리가 구할 총 동전 사용 개수(의 최솟값)

for n in range(N):
    value.append(int(input()))
    
value.sort(reverse=True)  # 큰 동전부터 계산하기 위해 내림차순 정렬

for v in value:        # 큰 동전부터
    if K == 0:
        break
    elif K // v != 0:  # 총 목표값을 이 동전값으로 나눠서 0이 아닐 때만
        num += K // v  # 그 몫을 더하고
        K %= v         # 그 나머지를 K에 할당해서 반복
        
print(num)
