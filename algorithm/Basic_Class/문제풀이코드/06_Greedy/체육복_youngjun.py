def solution(n, lost, reserve):
    answer = 0
    # answer_list를 n만큼 1로 초기화해준다.
    answer_list = [1] * n
    
    # 여벌 체육복 있는 학생들 체육복 1씩 더해줌
    for i in reserve:
        answer_list[i - 1] += 1
    
    # 체육복 도난당한 학생들 체육복 1씩 빼줌
    for j in lost:
        answer_list[j - 1] -= 1
    
    # 특정 학생이 여분의 체육복이 있고, 앞사람이 체육복을 도난당했거나, 뒷사람이 체육복을 도난당했을 경우 여분의 체육복이 있는 학생이 체육복을 앞사람 혹은 뒷사람에게 빌려준다.
    # 단, 첫번째 학생의 경우 앞사람이 없기 때문에, 여분의 체육복이 있고, 뒷사람이 체육복을 도난당했을 경우 뒷사람한테만 체육복을 빌려줄 수 있다.
    # 맨 끝 학생도 마찬가지로, 뒷사람이 없기 때문에, 여분의 체육복이 있고, 앞사람이 체육복을 도난당했을 경우 앞사람한테만 체육복을 빌려줄 수 있다.
    # 그 사이에 있는 사람등의 경우, 여분의 체육복이 있고, 앞사람, 혹은 뒷사람이 체육복을 도난당했을 경우 앞사람부터 체육복을 빌려준다.
    
    # 첫번째와 끝의 인덱스를 정의한다.
    left, right = 0, len(answer_list) - 1
    
    # 첫번째 학생이 체육복 여분을 가지고 있고, 바로 뒷사람이 도난당했을 경우, 뒷사람에게 체육복을 빌려준다.
    if answer_list[left] == 2 and answer_list[left + 1] == 0:
        answer_list[left] -= 1
        answer_list[left + 1] += 1
    
    # 사이에 있는 사람의 경우,
    for i in range(1, len(answer_list) - 1):
        # 특정 학생이 체육복 여분이 있을 경우
        if answer_list[i] == 2:
            # 바로 앞에 있는 사람부터 확인하여 도난당했으면
            if answer_list[i - 1] == 0:
                # 체육복을 빌려준다.
                answer_list[i] -= 1
                answer_list[i - 1] += 1
            # 앞사람 확인한 이후, 뒷사람이 체육복 도난당했으면
            elif answer_list[i + 1] == 0:
                # 체육복 빌려준다.
                answer_list[i] -= 1
                answer_list[i + 1] += 1
    
    # 맨 끝 학생이 체육복 여분을 가지고 있고, 바로 앞사람이 도난당했을 경우, 앞사람에게 체육복을 빌려준다.
    if answer_list[right] == 2 and answer_list[right - 1] == 0:
        answer_list[right] -= 1
        answer_list[right - 1] += 1
    
    # 모두 순회하고 나서, 체육복을 1개 이상 가지고 있는 학생의 수가 정답이다.
    for i in answer_list:
        if i != 0:
            answer += 1
    
    return answer
