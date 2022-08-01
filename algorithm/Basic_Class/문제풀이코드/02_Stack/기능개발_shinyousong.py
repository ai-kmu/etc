def solution(progresses, speeds):
    #뒤에서 빼서 앞으로 당기는 속도를 제외하자
    progresses.reverse()
    speeds.reverse()
    res = []
    while progresses != []:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        while len(progresses) != 0 and progresses[-1] >= 100:
            del progresses[-1]
            cnt += 1
        if cnt != 0:
            res.append(cnt)
    return res
