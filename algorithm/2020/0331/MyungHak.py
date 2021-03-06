"""
문제에서 주어진 동전은 모두 배수관계에 있다고 하였다. 
따라서 첫번째 항을 a1으로 두었을때 2번째나 3번째 항은 모두 a1*r로 이루어져 있을 것이다.
즉 작은동전 여러개가 모이면 큰것이 될 수 있다는 것이다.
이말을 바꾸어 말하면 작은 동전 여러개를 쓰는 것 보다 큰 동전하나를 사용하는 것이 문제를 푸는데 더 합리적이라는 것이다.
따라서 큰 동전만 우선하여 탐색하는 그리디 방법을 사용하면 된다.
"""

#우선 입력을 받아온다.
num, price = map(int, input().split())
arr = []
for i in range(num):
    arr.append(int(input()))


count = 0 #몇개의 동전을 사용할지 count한다.
for i in range(num-1,-1, -1): #이 때 큰 동전부터 탐색한다.
    if price >= arr[i]: #큰 동전부터 탐색했는데 현재 동전이 지금 내가 만들어야 하는 가격보다 낮은 경우
        coin = int(price / arr[i]) # 그 동전이 들어갈수 있는 최대치만큼
        price-=arr[i]*coin  # 지금 내가 만들어야 하는 가격에서 빼주고 
        count+=coin  # 이 코인의 개수를 count변수에 더해준다.
    if price == 0:  # 만약 현재 만들어야 하는 가격이 0원인 경우, 즉 내가 가진 코인을 이용하여 처음의 price값만큼을 만든 경우 반복문을 탈출해준다.
        break
print(count)
