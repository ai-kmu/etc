import sys

N, M, K = map(int, input().split())
secret = list(map(int, input().split()))
command = list(map(int, input().split()))

# dp를 위한 cnt리스트 생성
cnt = [[0]*M for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(M):
        """
         반복을 돌다 만약 비밀 레시피와 일치하는 커멘드가 있으면
         cnt에 이전까지 계산한 것을 더해줌
         i와 j가 0일 경우에는 i-1, j-1을 계산할 수 없기 때문에
         예외처리 해줌
        """
        if secret[i] == command[j]:
            if i == 0 or j == 0:
                cnt[i][j] = 1
            else:
                cnt[i][j] = cnt[i-1][j-1] + 1
            # 현재 계산한 값과 ans를 비교해 큰 값을 정답으로 설정
            ans = max(ans, cnt[i][j])

print(ans)
