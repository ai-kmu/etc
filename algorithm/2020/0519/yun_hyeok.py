def solution(answers):
    answer_1 = [1,2,3,4,5]
    answer_2 = [2,1,2,3,2,4,2,5]
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    mvp = []
    count_1, count_2, count_3 = 0, 0, 0
    for i, answer in enumerate(answers):
        if answer_1[i%len(answer_1)] == answer:
            count_1 += 1
        if answer_2[i%len(answer_2)] == answer:
            count_2 += 1
        if answer_3[i%len(answer_3)] == answer:
            count_3 += 1
    mvp_score = max(count_1, count_2, count_3)
    if count_1 == mvp_score: mvp.append(1)
    if count_2 == mvp_score: mvp.append(2)
    if count_3 == mvp_score: mvp.append(3)
        
    return mvp
