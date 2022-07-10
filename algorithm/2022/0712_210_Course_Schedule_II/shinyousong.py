#실패
from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if(numCourses == 0): return []
        if(numCourses == 0): return [0]

        #각 과목별로 선 이수 과목이 담긴 리스트 생성
        sortedPre = []
        for i in range(numCourses):
            temp = []
            for j in range(len(prerequisites)):
                if(prerequisites[j][0] == i): temp.append(prerequisites[j][1]) #과목별 선 이수 과목 담기
            sortedPre.append(temp)
        #이제 순서대로 선 이수 과목이 담긴 리스트가 생성되었음
        #최종 순서를 결정
        stack = []
        visited = [0 for i in range(numCourses)]
        Lst = [i for i in range(numCourses) if len(sortedPre[i]) != 0] #방문할 source
        Lst.reverse()
        print(sortedPre)
        print(Lst)
        while(Lst != []):
            temp = []
            idx = Lst.pop() #방문하고 있는 곳
            if(visited[idx] == 1): continue #방문한 곳이면 다음 곳으로
            temp.append(idx) #방문하지 않았다면 스택에 넣음
            visited[idx] = 1 #방문 표시
            for i in range(len(sortedPre[idx])):
                Lst.append(sortedPre[idx][i]) #방문해야 하는 곳을 전부 넣음
            temp.reverse() #스택이므로 뒤집기
            for i in temp:
                stack.append(i)
        for i in range(numCourses):
            if i not in stack: stack.append(i) #안 들어간 요소 넣어줌
        return stack
