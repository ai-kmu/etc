#자물쇠와 열쇠
#3:00

key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def solution(key, lock):
    answer = False

    lock_size=len(lock)
    key_size=len(key)

    extended_lock_size=lock_size*3-2 #기존 lock 공간 확장한 공간의 사이즈(가로 및 세로 길이)
    lock_extended=[[0 for col in range(extended_lock_size)]for row in range(extended_lock_size)]#기존 lock 공간 확장한 공간(2차원 배열)새로 만들기

    for i in range(0, lock_size): #확장한 새로운 lock공간 중간에 lock 값 복사하기
        for j in range(0, lock_size):
            lock_extended[i+lock_size-1][j+lock_size-1]=lock[i][j]

    end_point=extended_lock_size-key_size+1 #key mask 돌다가 멈출 지점

    m=0 #열, key가 lock_extended를 돌 때 어디까지 돌 수 있는지 체크하기 위함
    n=0 #행, 마찬가지
    isLockOpen=True #key에 의해 lock이 열렸는지 여부

    #lock_extended 배열 돌면서 lock을 key로 열어보는 작업
    while True:
        rotated_key=None #rotate된 key를 저장할 변수
        for rotate_num in range(0,4):# 0도, 90도, 180도 , 270도 순으로 4번에 걸쳐 한 key가 lock을 열 수 있는지 확인(회전은 총 3번)
            if rotate_num==0: #처음 key는 rotate안함
                rotated_key=key
            else:
                rotated_key = rotated(rotated_key) # key rotate하기

            for i in range(0, key_size): #1. lock에 key를 대보는 작업
                for j in range(0, key_size):
                    # print("보기:",i+m, j+n,"/",m,n)
                    lock_extended[i+m][j+n]+=rotated_key[i][j] # lock_extended값과 key값 더해주기

            #2. lock이 key에 의해 열렸는지 체크하는 작업
            for i in range(0, lock_size):
                for j in range(0, lock_size):
                    if lock_extended[i + lock_size - 1][j + lock_size - 1]!=1: # 만약 lock_extended값과 key값 더해준게 1과 다른 값이라면 (0 또는 2라면)
                        isLockOpen=False # lock과 key가 안맞는다는 뜻
                        break # 안 맞으니 이 key는 더 볼 필요 없구나!
                if isLockOpen==False: #한번 더 for문에서 탈출!
                    break

            #열렸는지 체크하는 작업에서 key가 lock과 맞은 경우
            if isLockOpen==True:
                answer=True #key가 lock을 열었다는 얘기니 답 True로 리턴
                return answer

            isLockOpen=True #다시 out_flag를 해결안된것으로 바꾸는 작업

            #원상복귀 작업1단계
            #lock_extended 값 원상복귀 하기(lock에 key 대보는 작업을 하면서 값이 달라져서 하는 것)
            for i in range(0, extended_lock_size):
                for j in range(0, extended_lock_size):
                    lock_extended[i][j]=0

            #원상복귀 작업2단계
            #다시 lock_extended에 lock 값 저장
            for i in range(0, lock_size):
                for j in range(0, lock_size):
                    lock_extended[i + lock_size - 1][j + lock_size - 1] = lock[i][j]

        #lock_extended 상에서 key 옮기는 작업(열로 먼저 훓고 그 다음 행 내려가는 순서로)
        n+=1 #열 기준으로 이동
        if n==end_point: #하나의 열 다돌았으면
            m+=1 #다음 행으로 이동
            n=0 #열은 0으로 초기화
        if m==end_point: #만약 모든 행을 다 돌았다면
            break #탐색 종료

    return answer

#key 회전 작업
def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    rotated_list=list([list(elem) for elem in list_of_tuples])
    return rotated_list

if __name__ == '__main__':
    print(solution(key,lock))