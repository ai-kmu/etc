"""
효율성을 해결해야 하는 문제 -> visit 판별을 주어진 maps에서 해결
"""

import collections

#각 영역에서 row,col,dep 값을 받아서 bfs 알고리즘 수행
def bfs(maps,start,end):
    queue = collections.deque([start])    #deque로 해야 queue보다 pop연산 시간이 적게 든다
    while queue:
        rowpos,colpos,dep = queue.popleft()   #현재 영역의 row,col,dep
        for rowmove,colmove in [(0,1),(0,-1),(-1,0),(1,0)]:   #현재 영역에서 갈수 있는 오른쪽,왼쪽,위,아래 영역
            rowchange = rowpos+ rowmove
            colchange = colpos+ colmove
            if rowchange == end[0] and colchange == end[1]:   #다음 영역이 목표지점일 경우
                return dep+1
            elif 0 <= rowchange < len(maps) and 0 <= colchange < len(maps[0]):    #다음 영역이 주어진 좌표값 안이여야 함 (-1,-1)은 불가능
                if maps[rowchange][colchange] == 1:     # 길이 있는경우
                    maps[rowchange][colchange] = 0      # visit 판단하기위해 해당영역을 길이 없는경우로 바꿔준다
                    queue.append((rowchange,colchange,dep+1))
    return -1        
            
   
def solution(maps):
    answer = 0
    start = (0,0,1)   # 시작지점 (0,0)에 첫시작점이니 dep =1
    end = (len(maps)-1,len(maps[0])-1)  #목표지점 (n,m)
    answer = bfs(maps,start,end)
    return answer
