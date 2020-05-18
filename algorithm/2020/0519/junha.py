def solution(answers):
   # 찍는 번호 및 변수 선언
    per1 = [1, 2, 3, 4, 5]
    per2 = [2, 1, 2, 3, 2, 4, 2, 5]
    per3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    corr_num = [0,0,0]
    answer = []

    # 일치하는 갯수 찾아내기
    for i in range(len(answers)):
        if answers[i] == per1[i%5]:
            corr_num[0] += 1
        if answers[i] == per2[i%8]:
            corr_num[1] += 1
        if answers[i] == per3[i%10]:
            corr_num[2] += 1

    # 가장 많이 맞춘학생은?
    max_cor = max(corr_num)
    for i in [1,2,3]:
        if corr_num[i-1] == max_cor:
            answer.append(i)

    return answer
