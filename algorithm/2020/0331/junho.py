coincategory , sumval = map(int,input().split())  #코인 종류 , 가치합 int로 저장
coinval = []
coinnum = 0
for coin in range(coincategory):                  #코인 종류별 값 int로 저장
  coin = int(input())
  coinval.append(coin)
for each in reversed(coinval):                    #코인 값이 큰거부터 비교
  if (each <= sumval):
    eachnum = int(sumval/each)                    #가치 합보다 작으면 그 코인의 개수
    sumval -= each * eachnum                      #가치 합에서 그 코인에 할당된 값 빼기
    coinnum += eachnum 
    if(sumval == 0):                              # 가치 합이 다 할당 된 경우 종료
      break;
print(coinnum)
