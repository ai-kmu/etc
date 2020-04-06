import numpy as np

def solution(key, lock):
    tiny_key = []
    tiny_lock = []
    size_key = len(key)
    size_lock = len(lock)
    N = 0
    blank_num = 0
    for i in range(size_key):
        for j in range(size_key):
            if key[i][j] == 1:
                tiny_key.append([i,j])
                N+=1
    for i in range(size_lock):
        for j in range(size_lock):
            if lock[i][j] == 0:
                tiny_lock.append([i,j])
                blank_num+=1
    
    if blank_num==0: #빈공간이 없는 경우
        return True
    elif blank_num > N: # 빈 공간이 열쇠의 홈보다 많은 경우
        return False
    
    rotate_key = [tiny_key]
    for i in range(3):
        T = []
        for j in range(N):
            T.append([rotate_key[i][j][1], -rotate_key[i][j][0]+size_key-1])  # rotate
        rotate_key.append(sorted(T))
    for i in range(4):    # 모든 회전에 대하여
        for j in range(N):  # 모든 key들을 각각 시작점으로 두고
            #tiny_lock은 0을 가지고 있는 좌표 rotate_key는 1을 가지고 있는 좌표
            
            
            distanceY = tiny_lock[0][0] - rotate_key[i][j][0]     #rotate_key[회전][시작점][x인지y인지]
            distanceX = tiny_lock[0][1] - rotate_key[i][j][1]     
            if len(rotate_key[i][j:]) < blank_num:
                break
            is_continue = False
            for Y,X in rotate_key[i][:j]:
                Y+=distanceY
                X+=distanceX
                if (Y >=0 and X >= 0 and Y<size_lock and X<size_lock):
                    if(lock[Y][X] == 1):
                        is_continue = True
            if is_continue:
                continue
            
            temp = j + 1
            fill_blank = 1
            while True:
                if fill_blank == blank_num:  # k가 모든 빈칸을 채운 경우
                    is_success = True
                    for Y,X in rotate_key[i][temp-1:]: #남아있는 돌기가 부딪치지 앉는지 확인
                        Y +=distanceY
                        X +=distanceX
                        if (Y >=0 and X >= 0 and Y<size_lock and X<size_lock):
                            if(lock[Y][X] == 1):
                                is_success = False
                    
                    if is_success:
                        return True
                    else:
                        break
                elif temp >= N:   # 열쇠의 모든 돌기를 사용한 경우
                    break
                elif ((distanceY == (tiny_lock[fill_blank][0] - rotate_key[i][temp][0])) 
                      and (distanceX == (tiny_lock[fill_blank][1] - rotate_key[i][temp][1]))): # 열쇠의 홈과 맞아떨어진 경우
                    fill_blank+=1 # 빈칸을 한칸 체움
                else:
                    Y = rotate_key[i][temp][0] + distanceY
                    X = rotate_key[i][temp][1] + distanceX
                    if (Y >=0 and X >= 0 and Y<size_lock and X<size_lock):
                        if(lock[Y][X] == 1):
                            break
                    
                    
                temp+=1 # 열쇠의 다음 홈을 탐색
    return False

