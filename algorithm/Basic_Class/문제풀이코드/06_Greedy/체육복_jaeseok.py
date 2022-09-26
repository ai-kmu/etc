def solution(n, lost, reserve):
    # 잃어버리기만 하고 여벌이 없는 사람들의 set
    nlost = set(lost) - set(reserve)
    # 여벌이 있고 잃어버리지도 않은 사람들의 set
    nreserve = set(reserve) - set(lost)
    # 총 학생 수에서 체육복을 빌릴 수 없는 사람을 빼가면 답
    answer = n
    # 잃어버린 사람의 번호에서 양옆에서 빌릴 수 있는 사람이 있는지 체크
    # 빌릴 수 있는 사람이 없으면 1씩 뺌
    for i in nlost:
        if i - 1 in nreserve:
            nreserve.remove(i-1)
        elif i + 1 in nreserve:
            nreserve.remove(i+1)
        else:
            answer -= 1
    return answer
