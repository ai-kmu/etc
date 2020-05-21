def solution(answers):
    answer = []
    # 수포자 3명의 찍는순서
    list = [[1,2,3,4,5],
           [2,1,2,3,2,4,2,5],
           [3,3,1,1,2,2,4,4,5,5]]
    corans = [0 for i in range(3)]
    #해당 문제에 각 수포자가 맞출경우 corans(list)에 맞춘문제수 count
    for id , val in enumerate(answers):
        for idx, i in enumerate(list):
            if val == i[id % len(i)]:
                corans[idx] += 1
    #가장 많이 맞힌 사람 구하기
    for id , val in enumerate(corans):
        if val == max(corans):
            answer.append(id+1)
            
    return answer
