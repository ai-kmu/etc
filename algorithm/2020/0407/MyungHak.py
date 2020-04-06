"""
상대 좌표계를 이용하여 문제를 풀었다.
1. 우선 Key를 나타내는 좌표계와 Lock을 나타내는 좌표계를 각각 잡는다
2. Key좌표계에서 Lock좌표계로 변환할 때 더해주어야 하는 변수를 (distanceX, distanceY)로 둔다.
3. Key의 각 돌기가 Lock의 좌표계로 좌표변환시 조건에 알맞는지 확인한다.
"""

import numpy as np
def is_possible(rotate_key, distanceY, distanceX, size_lock, lock):  # 현재 key의 돌기와 Lock의 돌기가 충돌하지는 않는지
    for Y,X in rotate_key:
        Y+=distanceY
        X+=distanceX
        if (Y >=0 and X >= 0 and Y<size_lock and X<size_lock):
            if(lock[Y][X] == 1):
                return False    
    return True


def solution(key, lock):
    tiny_key = [] # key의 돌기를 나타내는 좌표계, 벡터 형식으로 표현됨
    tiny_lock = [] # Lock의 홈을 나타내는 좌표계, 벡터 형식으로 표현됨
    size_key = len(key)
    size_lock = len(lock)
    N = 0
    blank_num = 0
    
    ################################### 좌표계로 변환#########################################
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
    ############################################################################################
                
    
    if blank_num==0: #빈공간이 없는 경우
        return True
    elif blank_num > N: # 빈 공간이 열쇠의 홈보다 많은 경우
        return False
    
    
    ################################# Rotation matrix를 이용한 좌표 변환 ############################
    rotate_key = [tiny_key]
    for i in range(3):
        T = []
        for j in range(N):
            T.append([rotate_key[i][j][1], -rotate_key[i][j][0]+size_key-1])  # 벡터 회전
        rotate_key.append(sorted(T))
    ###############################################################################################
    
    
    
    for i in range(4):    # 모든 회전에 대하여
        for j in range(N):  # 모든 key들을 각각 시작점으로 두고
            distanceY = tiny_lock[0][0] - rotate_key[i][j][0]     #rotate_key[회전][시작점][x인지y인지]
            distanceX = tiny_lock[0][1] - rotate_key[i][j][1]     
            
            if not is_possible(rotate_key[i][:j], distanceY, distanceX, size_lock, lock):
                continue
            
            temp = j + 1   # key의 j+1번째 돌기부터 시작
            fill_blank = 1 # 현재 lock의 빈칸을 하나 채움
            while True:
                if fill_blank == blank_num:    # k가 모든 빈칸을 채운 경우
                    if is_possible(rotate_key[i][temp-1:], distanceY, distanceX, size_lock, lock): # 만일 남은 열쇠의 돌기가 모두 lock의 돌기와 부딪치지 않는다면
                        return True
                    else:
                        break
                elif temp >= N:                # 열쇠의 모든 돌기를 사용한 경우
                    break
                elif ((distanceY == (tiny_lock[fill_blank][0] - rotate_key[i][temp][0])) 
                      and (distanceX == (tiny_lock[fill_blank][1] - rotate_key[i][temp][1]))): # 열쇠의 홈과 맞아떨어진 경우
                    fill_blank+=1              # 빈칸을 한칸 체움
                else:                          # 열쇠의 홈과 맞아떨어지지 않는경우 이것이 문제가 되는지 판단하고 그렇지 않으면 속행
                    if not is_possible([rotate_key[i][temp]], distanceY, distanceX, size_lock, lock):
                        break
                temp+=1 # 열쇠의 다음 홈을 탐색
    return False
