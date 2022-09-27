1. just 구현 

def solution(n, lost, reserve):
    answer = 0
    # answer_list를 n + 2만큼 1로 초기화해준다.
    answer_list = [1] * (n + 2)
    
    # 여벌 체육복 있는 학생들 체육복 1씩 더해줌
    for i in reserve:
        answer_list[i] += 1
    
    # 체육복 도난당한 학생들 체육복 1씩 빼줌
    for j in lost:
        answer_list[j] -= 1
    
    # 1번부터 부터 n번까지 순환하면서
    for i in range(1, n + 1):
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
    
    # 모두 순회하고 나서, 1번부터 n번까지 체육복을 1개 이상 가지고 있는 학생의 수가 정답이다.
    for i in answer_list[1 : n+1]:
        if i != 0:
            answer += 1
    
    return answer

2. 좀 더 greedy한 코드

def solution(n, lost, reserve):
    # 먼저 중복 제거
    # reserve와 lost에 둘 다 있는 학생은 결국 체육복이 하나밖에 없는 학생이므로, 체육복을 나눠주거나 받을 수 없다.
    # 따라서, reserve와 lost 집합을 만들고, 각각 차집합을 계산해 주면 중복 제거를 할 수 있다.
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    # 여분의 체육복을 가진 학생을 순회하면서
    for i in set_reserve:
        # 만약 앞번호에 체육복을 가지고 있는 사람이 있을 경우
        if (i - 1) in set_lost:
            # 체육복을 빌려줌(lost에서 없애줌)
            set_lost.discard(i - 1)
        # 만약 뒷번호에 체육복을 가지고 있는 사람이 있을 경우
        elif (i + 1) in set_lost:
            # 체육복을 빌려줌(lost에서 없애줌)
            set_lost.discard(i + 1)
        # 둘 다 아닐경우 continue
        else:
            continue

    return n - len(set_lost)
