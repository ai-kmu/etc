#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(brown, yellow):
    answer = []
    tile = brown + yellow
    yel_list = []
    # yellow_w * yellow_h = yellow 여야 한다
    # 여러가지 yellow_w 와 yellow_h 중에
    # yellow_w * 2 + yellow_h * 2 + 4 = brown 에 해당되는 yellow_w와 yellow_h를 찾아보자
    for i in range(1, yellow+1):
        if yellow % i == 0:
            yel_list.append(i)
    
    # 중앙을 기준으로 왼쪽은 높이 오른쪽은 너비로 정해줍니다.
    mid = len(yel_list) // 2
    yellow_h = []
    yellow_w = []
    
    # 모든 yellow 세로x가로 의 경우의 수를 구하기위해 모든 세로와 가로의 경우를 추가해주었습니다.
    if len(yel_list) % 2 == 0:
        for yh in yel_list[0:mid]:
            yellow_h.append(yh)
        for yw in yel_list[mid:len(yel_list)]:
            yellow_w.append(yw)
    if len(yel_list) % 2 != 0:
        for yh in yel_list[0:mid+1]:
            yellow_h.append(yh)
        for yw in yel_list[mid:len(yel_list)]:
            yellow_w.append(yw)        
    
    # 마지막으로 yellow_w * 2 + yellow_h * 2 + 4 = brown 에 해당되는 yellow_w와 yellow_h를 찾아보았습니다
    # 단, 세로x가로 의 값이 yellow의 값과 일치해야합니다.
    for i in range(1, yellow+1):
    for i in yellow_h:
        for j in yellow_w:
            if i * 2 + j * 2 + 4 == brown:
                if i*j == yellow:
                    
                    answer.append(j + 2)
                    answer.append(i + 2)
    
    
    return answer

