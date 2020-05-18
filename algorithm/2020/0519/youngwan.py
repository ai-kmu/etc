def solution(answers):
    a = [1, 2, 3, 4, 5]                  # 1번 수포자
    a_num = 0
    b = [2, 1, 2, 3, 2, 4, 2, 5]         # 2번 수포자
    b_num = 0
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]   # 3번 수포자
    c_num = 0
    answer_dic = {1:0, 2:0, 3:0}         # 정답 dictionary

    for i in answers:                    # 각 정답마다

        if i == a[a_num]:                # 찍은 정답과 같은지 비교하고
            answer_dic[1] += 1           # 같다면 dictionary에 추가
        if a_num == len(a) - 1:          # 다음 번호로 넘어간다
            a_num = 0
        else:
            a_num += 1

        if i == b[b_num]:
            answer_dic[2] += 1
        if b_num == len(b) - 1:
            b_num = 0
        else:
            b_num += 1

        if i == c[c_num]:
            answer_dic[3] += 1
        if c_num == len(c) - 1:
            c_num = 0
        else:
            c_num += 1
            
    answer_dic = sorted(answer_dic.items(), key=lambda item: item[1], reverse=True)   # 정답 횟수를 많은 순서로 정렬하고
    answer = []
    big = 0
    for key, value in answer_dic:        # dictionary에 대해
        if big == 0:                     # 첫 번째 값에 대해서는
            big = value                  # 값을 저장하고
            answer.append(key)           # answer에 추가
        else:                            # 다른 값들에 대해서는
            if big == value:             # 정답 횟수가 같다면
                answer.append(key)       # answer에 추가

    return answer
