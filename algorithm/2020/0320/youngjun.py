#7:40~

priorities=[2,1,3,2]
location=2

def solution(priorities, location):
    answer = 0
    #priorities가 stack역할
    max_value = max(priorities)

    while True:

        pop_element = priorities.pop(0)


        if max_value == pop_element: #만약, 현재 값이 제일 큰 값이라면

            answer += 1 # 횟수 증가

            if location == 0: #만약 현재 값이 인쇄 요청한 문서이면
                break #인쇄 요청한 문서가 프린트 되었으니 종료
            else: #만약 현재 값이 인쇄 요청한 문서가 아니라면
                location -= 1
            max_value = max(priorities) #max인 숫자가 빠져나갔으니까 max갱신

        else: #만약, 현재 값이 제일 큰 값이 아니라면
            priorities.append(pop_element) #stack 뒤에 추가
            if location == 0: #현재 값이 우리가 인쇄 요청한 문서이면
                location = len(priorities) - 1 #인쇄 요청한 문서의 위치를 stack 맨 밑으로 보냄
            else: # 현재 값이 우리가 인쇄 요청한 문서가 아니라면
                location -= 1 #인쇄 요청한 문서의 위치를 위로 옮김

    return answer

if __name__ == '__main__':
    solution(priorities,location)