#자물쇠와 열쇠
#3:00

key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def solution(key, lock):
    answer = False

    lock_size=len(lock)
    key_size=len(key)

    extended_lock_size=lock_size*3-2 #기존 lock 공간 확장한 공간의 사이즈(가로 및 세로 길이)
    lock_extended=[[0 for col in range(extended_lock_size)]for row in range(extended_lock_size)]#1. 기존 lock 공간 확장한 공간(2차원 배열)새로 만들기

    for i in range(0, lock_size): #2. 확장한 새로운 lock공간 중간에 lock 값 복사하기
        for j in range(0, lock_size):
            lock_extended[i+lock_size-1][j+lock_size-1]=lock[i][j]

    end_point=extended_lock_size-key_size+1 #key mask 돌다가 멈출 지점

    row=0 #행, key가 lock_extended를 돌 때 어디까지 돌 수 있는지 체크하기 위함
    col=0 #열, 마찬가지
    isLockOpen=True #key에 의해 lock이 열렸는지 여부

    #3. lock_extended 배열 돌면서 lock을 key로 열어보는 작업
    while True:
        rotated_key=None #rotate된 key를 저장할 변수
        for rotate_num in range(4):# 0도, 90도, 180도 , 270도 순으로 4번에 걸쳐 한 key가 lock을 열 수 있는지 확인(회전은 총 3번)
            if rotate_num==0: #처음 key는 rotate안함
                rotated_key=key
            else:
                rotated_key = rotated(rotated_key) # key rotate하기

            for i in range(0, key_size): #3-1. lock에 key를 대보는 작업
                for j in range(0, key_size):
                    # print("보기:",i+row, j+col,"/",row,col)
                    lock_extended[i+row][j+col]+=rotated_key[i][j] # lock_extended값과 key값 더해주기

            #3-2. lock이 key에 의해 열렸는지 체크하는 작업
            for i in range(0, lock_size):
                for j in range(0, lock_size):
                    if lock_extended[i + lock_size - 1][j + lock_size - 1]!=1: # 만약 lock_extended값과 key값 더해준게 1과 다른 값이라면 (0 또는 2라면)
                        isLockOpen=False # lock과 key가 안맞는다는 뜻
                        break # 안 맞으니 이 key는 더 볼 필요 없구나!
                if isLockOpen==False: #한번 더 for문에서 탈출!
                    break

            #3-3. 열렸는지 체크하는 작업에서 key가 lock과 맞은 경우
            if isLockOpen==True:
                answer=True #key가 lock을 열었다는 얘기니 답 True로 리턴하고 종료
                return answer

            #3-4. 안 열렸다면 원상복귀 작업
            #원상복귀 작업1단계
            isLockOpen = True  # 다시 out_flag를 해결안된것으로 바꾸는 작업
            #3-4-1. lock_extended 값 원상복귀 하기(lock에 key 대보는 작업을 하면서 값이 달라져서 하는 것)
            for i in range(0, extended_lock_size):
                for j in range(0, extended_lock_size):
                    lock_extended[i][j]=0

            #원상복귀 작업2단계
            #3-4-2. 다시 lock_extended에 lock 값 저장
            for i in range(0, lock_size):
                for j in range(0, lock_size):
                    lock_extended[i + lock_size - 1][j + lock_size - 1] = lock[i][j]


        #key 4번 회전하면서 열리는지 체크하고 안열리면 key를 lock_extended상에서 이동
        #lock_extended 상에서 key 옮기는 작업(열로 먼저 훓고 그 다음 행 내려가는 순서로)
        col+=1 #열 기준으로 이동
        if col==end_point: #하나의 열 다돌았으면
            row+=1 #다음 행으로 이동
            col=0 #열은 0으로 초기화
        if row==end_point: #만약 모든 행을 다 돌았다면
            break #탐색 종료

    return answer

#key 회전 작업
def rotated(array_2d):
    # array_2d[::-1] : 2차원 배열의 순서를 거꾸로 변경
    # *array_2d[::-1] : 거꾸로 변경한 다음 감싸고 있는 리스트를 unpack하고 각각의 안에 있던 요소들(여기선 리스트)을  각각의 요소로 변경함
    #zip : 주어진(iterable한 리스트나 dictionary등) 각각의 요소(여기선 리스트)를 사용해, index 기준으로 묶음
    list_of_tuples = zip(*array_2d[::-1])
    #새로 묶은 요소들을 list로 감쌈
    rotated_list=list(list_of_tuples)

    return rotated_list

if __name__ == '__main__':
    print(solution(key,lock))







# 재빈 코드=========================================================================================================


# 15. 프로그래머스 - 자물쇠와 열쇠
import numpy as np

# 90도 회전 ... numpy
def rotation(arr, angle):
    rotate_key = np.rot90(arr, 3-angle) # 원래 왼쪽으로 회전하는데, 오른쪽으로 회전하게 만듬
    return rotate_key

# 자물쇠 열리는지 확인
def check(startX, startY, key, lock, p_size, start, end):
    pad = [[0] * p_size for _ in range(p_size)] #lock을 확장한 padding 만들기(일단 모두 0으로 채워줌)
    print("pad",pad)
    print("================")
    # padding 초기화
    #1.padding 영역에 key 값 더하는 과정
    for i in range(len(key)):#key크기만큼 돌면서
        for j in range(len(key)):
            pad[startX+i][startY+j] += key[i][j]#padding영역값에 key값 더하기

    #2. padding영역 상에 더해준 key값과 lock값을 더해서 해당 key가 lock을 열수있는지 아닌지 판단하는 과정
    for i in range(start, end):
        for j in range(start, end):
            pad[i][j] += lock[i - start][j - start] #padding영역 상에 더해준 key값과 lock값을 더함
            if pad[i][j] != 1: #만약 1이 아니라면, 홈과 돌기가 맞물리지 않았다는 얘기(key가 lock을 못 열음)
                return False # key가 lock을 못 열으니까 False 리턴

    return True # key가 lock을 열으면 True 리턴


def solution(key, lock):
    answer = False

    # lock의 시작점과 끝나는 지점
    start = len(key) - 1 #lock의 시작점
    end = start + len(lock) #lock의 끝나는 지점

    # padding이 추가된 배열의 행, 열의 크기
    pad_size = len(lock) + start * 2 #아까 lock_extended와 같은 개념

    # 4가지만 비교 0, 90, 180, 270
    for a in range(4): #회전 0도, 90도, 180도, 270도 총 4번 하면서 ( 0도 회전한 키로 padding 한번 쭉 검사하고, 90도 회전한 키로 padding 한번 쭉 검사하는 방식)
        for i in range(end): #lock이 끝나는 지점까지
            for j in range(end):  #lock이 끝나는 지점까지
                if check(i, j, key, lock, pad_size, start, end): #해당 key가 lock을 열수 있는지 판단
                    answer = True #열 수 있으면 answer는 True
        # key = rotate(key)
        key = rotation(key, a) # key를 회전할 때 몇도 회전할건지 a로 조절
    return answer

key_1 = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock_1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key_1, lock_1))
