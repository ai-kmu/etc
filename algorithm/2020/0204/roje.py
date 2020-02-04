iteration = int(input())
maps = [[0]*101 for i in range(101)]
answer = [0] * (iteration+1)

for iters in range(1, iteration+1):
  x, y, width, height = map(int, input().split())
  for row in range(x, x + width):
    for col in range(y, y + height):
      maps[row][col] = iters
