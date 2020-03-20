def solution(priorities, location):
    final = []
    answer = 0
    while priorities != []:
        max_ = max(priorities)
        first = priorities.pop(0)
        if max_ == first:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
        else:
            priorities.append(first)
            if location == 0:
                location = len(priorities) - 1  # 젤 뒷 인덱스
            else:
                location -= 1 #한칸 땡김
    return answer
