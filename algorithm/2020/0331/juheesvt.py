# 입력
N, K = map(int,input().split())
inp = [int(input()) for i in range(N)]

# 초기화
count = 0

# 처리 -> 큰 금액의 종류인 코인부터 거슬러주면 최소한의 갯수로 코인의 갯수가 나온다.
for idx, coin in enumerate(reversed(inp)):
    # 코인의 종류가 현재 남은 금액보다 작거나 같을 때,
    if K >= coin:
        # 코인의 종류로 남은금액을 나눠주면 해당 종류의 코인이 몇개인지 나오고 그걸 총 코인 갯수에 더한다.
        count += int(K / coin)
        # 거슬러준만큼 남은금액에서 빼준다.
        K = K % coin
print(count)
