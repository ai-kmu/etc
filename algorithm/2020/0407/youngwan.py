import copy

#key를 시계방향으로 돌리는 함수
#한 행을 회전시켜 열로 바꾼다
def turn(key):
    temp = [[0 for i in range(len(key))] for i in range(len(key))]
    for i in range(len(key)):
        #바꿔줄 열 설정
        line = len(key) - 1 - i
        for j in range(len(key[i])):
            #정한 열에 key의 한 행을 넣어준다
            temp[j][line] = key[i][j]
    return temp


#lock의 크기를 (key의 크기-1)만큼 확장하는 함수
#lock가 3*3, key가 3*3인 경우 새로운 lock의 크기는 7*7
def resize(key, lock):
    #위에 key-1만큼의 열은 0으로 채운다
    newlock = [[0 for i in range((len(key)-1)*2+len(lock))] for i in range(len(key)-1)]
    #lock이 들어갈 줄은 앞을 key-1만큼을 0으로 채우고 lock을 넣고 뒤를 key-0만큼 채운다
    for i in lock:
        newlock.append([0 for i in range(len(key)-1)]+ i + [0 for i in range(len(key)-1)])
    #아래 key-1만큼의 열은 0으로 채운다
    for i in range(len(key)-1):
        newlock.append([0 for i in range((len(key)-1)*2+len(lock))])
    return newlock


#lock에 key를 더하는 함수
def fit(key, lock):
    #lock이 열쇠없이도 열리는지 확인
    fit_answer = check(key, lock)
    if fit_answer:
        return fit_answer
    col = 0
    row = 0
    num = 0
    #현재 lock는 확장된 상태 - key의 크기-1 만큼
    #(확장된 lock의 크기 - (key의 크기-1))**2만큼 반복하면 열쇠를 움직이면서 모두 넣어볼 수 있다
    for i in range((len(lock)-(len(key)-1))**2):
        templock = copy.deepcopy(lock)
        # 한 행의 검사가 끝나면 다음 행으로 넘어간다
        if num%(len(lock)-len(key)+1) == 0:
            if num != 0:    
                col += 1 
                row = 0
        #새로운 시작점을 temp_col과 temp_row에 저장
        temp_col = col
        temp_row = row
        #lock에 key를 더해준다
        for i in key:
            for j in i:
                templock[temp_col][temp_row] += j
                temp_row += 1
            temp_col += 1
            temp_row = row
        #열쇠가 맞는지 확인
        fit_answer = check(key, templock)
        if fit_answer:
            break
        #다음 열로 넘어간다
        row += 1
        num += 1
    return fit_answer


#열쇠가 맞는지 확인하는 함수
def check(key, lock):
    #시작은 (key의 크기-1, key의 크기-1)에서 시작
    col = len(key)-1
    row = len(key)-1
    for i in range(len(lock)-(len(key)-1)*2):
        for j in range(len(lock)-(len(key)-1)*2):
            #현재 위치가 1인지 아닌지 확인
            if lock[col][row] !=1:
                return False
            #다음 열 확인
            row += 1
        #다음 행 확인, 열은 key의 크기-1로 돌아감
        col += 1
        row = len(key)-1
    #확인한 모든 곳이 1이라면 True를 반환
    return True


def solution(key, lock):
    answer = False
    #lock의 크기를 확장
    lock = resize(key, lock)
    #총 3번의 회전을 실행
    for i in range(4):
        #key가 lock에 맞는지 확인
        answer = fit(key, lock)
        if answer == True:
            break
        #key를 한번 회전
        key = turn(key)
    return answer
