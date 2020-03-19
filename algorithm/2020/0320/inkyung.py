def solution(priorities, location):
    answer= 0
    #가장 큰 값 출력
    most_impt = max(priorities)
    
    while True:
        #가장 앞에 있는 문서를 대기 목록에서 꺼냄
        first = priorities.pop(0)
        
        #만약 J가 가장 중요한 문서라면 answer += 1
        #만약 location이 0 이라면 정답이 1인상태로 출력 되어야 함
        #pop()을 사용했기 때문에 most_impt갱신
        if first == most_impt:
            answer += 1
            if location == 0:
                break
            location -= 1
            most_impt = max(priorities)
        #만약 first != most_impt이면 J를 뒤로 보내줘야 함
        else:
            priorities.append(first)
            if location == 0:
                location  = len(priorities) - 1
            else:
                location -= 1
    return answer
