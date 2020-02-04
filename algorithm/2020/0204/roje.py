# 색종이 몇 장
iteration = int(input())
# 평면
maps = [[0]*101 for i in range(101)]
answer = [0] * (iteration+1)

# 1부터 시작
for iters in range(1, iteration+1):
  x, y, width, height = map(int, input().split())
  for row in range(x, x + width):
    for col in range(y, y + height):
      maps[row][col] = iters

# 평면 리스트를 돌면서
for iters in maps:
  for num in iters:
    # 0 이 아니면
    if num:
      # 해당 숫자의 개수를 1씩 증가
      answer[num] += 1

# 1
for ans in answer[1:]:
  print(ans)
