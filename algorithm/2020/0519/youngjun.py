#모의 고사
# 4:51 ~ 5:19

answers=[1,3,2,4,2]

def solution(answers):
    answer = []
    peopleAnswerList=[[1,2,3,4,5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    maxAnswerCount=0
    #1번 수포자 맞은 문제 계산
    for idx, personAnswer in enumerate(peopleAnswerList):
        currentAnswerCount=checkAnswer(personAnswer,answers)
        if currentAnswerCount>maxAnswerCount:
            if len(answer)!=0:
                answer.clear()
            answer.append(idx+1)
            maxAnswerCount=currentAnswerCount

        elif currentAnswerCount==maxAnswerCount:
            answer.append(idx+1)

    print(answer)
    return answer

def checkAnswer(list,answers):
    listLength=len(list)
    correctCount=0
    listIndex=0
    for answer in answers:
        if answer==list[listIndex]:
            correctCount+=1

        listIndex+=1
        if listIndex==listLength:
            listIndex=0

    return correctCount

if __name__ == '__main__':
    solution(answers)