#아이디어 : 2:08~2:24
#구현 : 2 :33~3:30

#dfs로 구현

def solution(n, computers):
    answer = 0

    #전체 그래프 노드 리스트(나중에 경로가 끊긴 경우 다른 경로에 있는 노드를 찾기 위함)
    totalGraph=[]
    for i in range(0, n):
        #노드를 추가함
        totalGraph.append(i)

    #방문할 노드 리스트 (stack역할)
    toVisit=[]

    #방문한 노드 리스트
    visited=[]

    #그래프안의 모든 노드 돌면 빠져나옴
    while totalGraph:
        #네트워크 수 증가
        answer+=1
        #전체 그래프에서 첫번째 노드를 방문할 노드 리스트에 추가
        toVisit.append(totalGraph[0])

        #빠져나오면 경로가 끊긴 경우
        while toVisit:
            #방문할 현재 노드, 현재 노드는 방문할 노드에서 제거
            currentNode=toVisit.pop()
            #방문했으니 전체 노드 그래프에서 제거
            totalGraph.remove(currentNode)
            #방문했으니 방문한 노드 리스트에 추가
            visited.append(currentNode)

            #2차원 배열의 index를 알기 위해 사용
            index = 0
            #현재 노드와 연결된 다른 노드 탐색
            for i in computers[currentNode]:
                #다른 노드가 현재노드와 1(연결되어)있고, 다른노드가 방문할 노드와 방문한 노드에 모두 없는경우
                if i ==1 and index not in toVisit+visited:
                    #다른 노드를 방문할 노드 리스트에 추가
                    toVisit.append(index)
                index+=1

    return answer



if __name__=="__main__":
    n=3
    computers=[[1,1,0],[1,1,1],[0,1,1]]
    print(solution(n,computers))

