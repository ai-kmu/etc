import math
progresses = [93,30,55]
speeds = [1,30,5]
answer = []
complete_day = []

for i in range(len(progresses)):
    temp = math.ceil((100 - progresses[i]) / speeds[i] )
    complete_day.append(temp)
    # print(complete_day)

first_of_each_distri = complete_day[0]
num = 0
answer = []
for i in complete_day:
    if first_of_each_distri < i:
        answer.append(num)
        num = 1
        first_of_each_distri = i
    else :
        num += 1

answer.append(num)
print(answer)
