def solution(answers):
    student = [[1,2,3,4,5], [2,1,2,3,2,4,2,5] ,[3,3,1,1,2,2,4,4,5,5]]  #수포자 패턴 초기화  
    scores = [0,0,0]
    
    for i in range(len(answers)):  
        for j, stu in enumerate(student):
            if answers[i] == stu[i % len(stu)]:  # 정답과 일치할경우 score 더하기
                scores[j] += 1
                
    return [i+1 for i, x in enumerate(scores) if x == max(scores)]  #가장 max한 점수를 가지는 학생 리턴
