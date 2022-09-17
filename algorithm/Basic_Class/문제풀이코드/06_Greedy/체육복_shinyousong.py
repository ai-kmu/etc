def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    # 자기->앞->뒤 순으로 빌리기 시도
    for lostman in lost:
        if lostman in reserve:
            del reserve[reserve.index(lostman)]
            answer += 1
        elif lostman - 1 in reserve:
            del reserve[reserve.index(lostman - 1)]
            answer += 1
        # 뒷사람이 못빌려주는 경우
        elif lostman + 1 in reserve:
            if not lostman + 1 in lost:
                del reserve[reserve.index(lostman + 1)]
                answer += 1
    return answer
