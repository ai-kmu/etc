import numpy as np

def solution(key, lock):
    answer = False
    N = len(lock)           # 자물쇠의 크기
    M = len(key)            # 열쇠의 크기
    keyweight = np.array(key)
    lockpool = np.zeros((N+2*M-2 , N+2*M-2))    # key를 weight로 갖는 convolution 연산으로 처리하기위해 자물쇠를 0으로 padding해줌
    
    fillblock = 0     # 자물쇠에서 열쇠가 들어가야하는 block 수(* -값)
    for i in range(N):
        for j in range(N):
            if(lock[i][j] == 0):          # 자물쇠에서 열쇠가 들어가야하는 공간은 -1값을 가지게함
                lockpool[M-1+i][M-1+j] = -1
                fillblock -= 1        
            else:
                lockpool[M-1+i][M-1+j] = lock[i][j]       # 자물쇠에서 block이 차있는 곳은 1값
                
    
    for i in range(4):        # 키를 90도씩 회전할경우 총 4번의 다른 수행
        for j in range(N+M-1):        # keyweight가 lockpool에서 1씩 이동
            for k in range(N+M-1):    
                sum = 0       # convolution 연산 결과
                for num1 in range(M):
                    for num2 in range(M):
                        sum += keyweight[num1][num2] * lockpool[j+num1][k+num2]
                        
                if (sum == fillblock):    # block이 겹치지않고 열쇠가 빈부분을 차지하는 경우
                    answer = True
                    return answer
        keytrans = keyweight.T      # key를 전치하고 각 행을 역순하면 90도 전환한것과 동일
        keyweight = keytrans[:,::-1]
                    
    return answer
