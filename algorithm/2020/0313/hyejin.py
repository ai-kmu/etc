import math


def solution(progresses, speeds):
    answer = []
    # front: 앞작업의 작업기간
    # count: 하루마다 배포할 기능의 개수
    front = 0
    count = 0
    # 매번 length를 구하면 시간이 들어서 미리 계산해둠.
    num_job = len(progresses)
    for i in range(len(progresses)):
        # 걸리는 기간 계산
        period = math.ceil((100 - progresses[i]) / speeds[i])
        if i == 0:
            front = period
            count = 1
            continue
        # i번째 작업이 앞작업보다 일찍 끝나거나 같이 끝날 때 => 앞작업과 같이 배포 가능
        if period <= front:
            count += 1
            if i == num_job - 1:
                answer.append(count)
            continue
        # i번쨰 작업이 앞작업보다 늦게 끝날 때 => 다음 배포 때 가능
        else:
            front = period
            answer.append(count)
            count = 1
            if i == num_job - 1:
                answer.append(count)

    return answer
