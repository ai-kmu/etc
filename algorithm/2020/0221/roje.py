# 수빈이와 동생 숨바꼭질
# 수빈이가 동생의 위치까지 가는데 몇초가 걸리는지를 구해야 함
# 수빈이와 동생의 위치의 범위 : [0, 100,000]

# 수빈이의 위치, 동생의 위치를 입력으로 받음
subin, younger = map(int, input().split())

# 수빈이는 이동시 1초후에 '현위치-1 혹은 현위치+1' 로 이동이 가능
# 순간이동시 0초후에 현위치*2 로 이동이 가능

# subin == yonger
if subin == younger:
  print(0)

# subin > younger -> 무조건 subin - 1로 이동!!
elif subin > younger:
  print(subin - younger)
  
# subin < younger -> 복잡해짐...
else:
  # 배열을 만들어서 각 위치에 도달할 최소 거리를 입력해줌
  game_map = [0 for i in range(younger+1)]
  for i in range(0, subin+1):
    game_map[i] = subin - i
  
  for idx in range(subin+1, younger+1):
    if idx % 2 == 0:
      game_map[idx] = min(game_map[idx-1]+1, game_map[idx//2])
    else:
      game_map[idx] = min(game_map[idx-1]+1, game_map[(idx+1)//2]+1, game_map[(idx-1)//2]+1)
    for _ in range(idx, 1, -1):
      if game_map[_] - game_map[_-1] >= 2:
        game_map[_] = game_map[_-1] + 1
      else:
        break
  print(game_map[younger])
