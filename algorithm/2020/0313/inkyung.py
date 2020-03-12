def solution(progresses, speeds):
    left = list()
    for i in range(len(progresses)):
        temp = (100 - progresses[i]) // speeds[i]
        if (temp * speeds[i]) + progresses[i] == 100:
            left.append(temp)
        else:
            left.append(temp + 1)
    first = left[0]
    answer = []
    num = 0
    for i in range(len(progresses)):
        if first >= left[i]:
            num += 1
        else:
            answer.append(num)
            first = left[i]
            num = 1
    answer.append(num)
    return answer

