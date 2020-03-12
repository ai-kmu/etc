#기능개발
#10:40~11:17

progresses=[93,30,55]
speeds=[1,30,5]

def solution(progresses, speeds):
    answer = []

    finishDays=[]
    for i in range(0, len(progresses)):

        quotient=int((100-progresses[i])/speeds[i])
        remainder=(100-progresses[i])%speeds[i]

        if quotient==0:
            finishDays.append(1)
        elif remainder:
            finishDays.append(quotient+1)
        else:
            finishDays.append(quotient)

    max=-1
    count=1
    for day in finishDays:

        if max==-1:
            max=day
            continue
        if day<=max:
           count+=1
        else :
            answer.append(count)
            max=day
            count=1
    answer.append(count)

    return answer

if __name__ == '__main__':
    solution(progresses,speeds)