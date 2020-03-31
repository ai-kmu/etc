N, K = map(int, input().split())
money = [int(input()) for _ in range(N)]

answer = 0 #동전의 최소 갯수

for i in range(1, N+1):
    #인덱스 끝에서부터 시작
    coin = money[-i]

    #인덱스 값 보다 클 때 그 값으로 나눠서 동전 갯수 구하기
    if K >= coin:
        num = K // coin #필요한 동전 갯수 몫 구하기
        K -= num*coin
        answer += num

print(answer)
