days, rice_cake = list(map(int, input().split()))

fibo = [1,1]
for i in range(2, days - 1):
  fibo.append(fibo[i-1] + fibo[i - 2])

for first_day in range(1,rice_cake):
  second_day = (rice_cake - fibo[days-3] * first_day)/fibo[days - 2]
  if  second_day == int(second_day):
    print(int(first_day))
    print(int(second_day))
    break;
