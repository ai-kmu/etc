num = int(input())


maps = []
for i in range(101):
  temp_arr = [0 for i in range(101)]
  maps.append(temp_arr) 



for i in range(num):
  x1,y1,X,Y = map(int, input().split())
#  print(x1)
#  print(y2)


  
  for j in range(x1, x1+X):
    for k in range(y1, y1+Y):
      maps[k][j] = i+1

count = 0
for k in range(1, num + 1):
  for i in range(101):
    for j in range(101):
      if(maps[j][i] == k):
        count+=1
  print(count)
  count = 0
