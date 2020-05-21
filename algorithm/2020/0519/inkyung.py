#만약 answer의 길이가 더 길다면 person의 길이를 answer의 길이와 같거나 크게 만들어야함
def len_comparison(answer, person):
    if len(answer) > len(person):
        return person * (len(answer) // len(person) + 1)
    else:
        return person

#반복문을 수행하면서 answer와 person의 정답이 같다면 점수를 획듣
def score_accum(answer, person):
    temp = 0
    for i in range(len(answer)):
        if answer[i] == person[i]:
            temp += 1
    return temp
    
def solution(answers):
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    answer = []

    #각각 정답 비교
    person_1 = len_comparison(answers, person_1)
    score[0] = score_accum(answers, person_1)

    person_2 = len_comparison(answers, person_2)
    score[1] = score_accum(answers, person_2)

    person_3 = len_comparison(answers, person_3)
    score[2] = score_accum(answers, person_3)
    
    for idx,s in enumerate(score):
        if s == max(score):
            answer.append(idx + 1)
    return answer
