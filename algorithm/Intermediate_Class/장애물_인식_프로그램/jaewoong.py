#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#탐색을 십자가형태로, 다음 칸에 있을경우 다시 탐색, 재귀호출하는 형식
#재귀호출은 상황에 따라 변동하나, 전체적인 틀은 같은 틀을 반복해야 할때 쓰임
def dfs(x,y):
    #영역을 벗어나는 경우, 돌아가게 한다.
    if x<= -1 or x>=n or y<=-1 or y>=n:
        return False
    #방문하지 않은 노드의 경우
    if graph[x][y] ==1:
        cnt.append(0) #블록의 개수를 세기위해 리스트에 아무 요소를 넣어주고, 요소의 개수만큼 블록 개수를 확인한다.
        graph[x][y] = 0 #해당노드를 방문처리 (1>0으로 바꿔주면)
        #십자가 형태 재귀적으로 탐색
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n = int(input()) #지도의 크기
cnt = []
graph = [] #맵 정보 받는다
for i in range(n):#인풋값을 map함수를 통해 정보를 입력받는다
    graph.append(list(map(int,input())))

#모든 위치에 대해 장애물 블록을 만든다.
result=0
result_list=[]
for i in range(n):
    for j in range(n):
        #dfs 수행
        #탐색 중 블록의 시작이 확인되는 경우
        if dfs(i,j) == True:
            result += 1
            #cnt길이를 통해 장애물의 개수 확인
            result_list.append(len(cnt))
            cnt = []
#총 블록의 수 출력            
print(result)
#장애물의 수 정렬 후 출력(sort)
result_list.sort()
for i in result_list:
    print(i)


# In[ ]:





# In[ ]:




