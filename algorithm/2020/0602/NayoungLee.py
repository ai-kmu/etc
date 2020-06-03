timelist = []
for i in range(11):
    time = list(input().split())
    timelist.append(time)

timelist.sort() #시간리스트 정렬
count = 0
penality = 0
verdicts = 0 
for j in range(len(timelist)):
    penality += int(timelist[j][0]) #각 문제에서의 패널티들의 합
    count += penality #구하고자 하는 총 패널티의 합
    verdicts += int(timelist[j][1]) #못푼문제의 패널티 추가
    
answer = count + verdicts*20
print(answer)
