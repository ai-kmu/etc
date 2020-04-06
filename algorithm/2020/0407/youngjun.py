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

    m=0 #열
    n=0 #행
    out_flag=True

    #lock_extended 돌면서 lock을 key로 열어보는 작업
    while True:
        rotated_key=None
        for rotate_num in range(0,4):
            # print("회전",rotate_num)
            if rotate_num==0:
                rotated_key=key
            else:
                rotated_key = rotated(rotated_key)

            for i in range(0, key_size): #1. lock에 key를 대보는 작업
                for j in range(0, key_size):
                    # print("보기:",i+m, j+n,"/",m,n)
                    lock_extended[i+m][j+n]+=rotated_key[i][j]

            #2. 열렸는지 체크하는 작업 //여기서 뭐가 문제 있는지확인하기 (열렸는지 체크하는 작업이 잘못된듯)
            for i in range(0, lock_size):
                for j in range(0, lock_size):
                    if lock_extended[i + lock_size - 1][j + lock_size - 1]!=1:
                        out_flag=False
                        break
                if out_flag==False:
                    break

            #열렸는지 체크하는 작업에서 key가 lock과 맞은 경우
            if out_flag==True:
                answer=True #key가 lock을 열었다는 얘기니 탈출
                return answer

            out_flag=True #다시 out_flag를 해결안된것으로 바꾸는 작업

            #원상복귀
            for i in range(0, len(lock_extended)):
                for j in range(0, len(lock_extended)):
                    lock_extended[i][j]=0

            for i in range(0, lock_size):
                for j in range(0, lock_size):
                    lock_extended[i + lock_size - 1][j + lock_size - 1] = lock[i][j]

        #key mask 옮기는 작업
        n+=1
        if n==end_point:
            m+=1
            n=0
        if m==end_point:
            break

    return answer

#회전
def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    rotated_list=list([list(elem) for elem in list_of_tuples])
    return rotated_list

if __name__ == '__main__':
    print(solution(key,lock))