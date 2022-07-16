#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result=[] # 정답을 넣기위한 배열
        def search(treenode): # 노드를 탐색하는 함수
            if(treenode==None): # 빈 노드일 경우(null)
                return #탐색을 끝낸다. 트리의 특성상 노드가 비어있으면 다음 노드로 연결이 안되기때문
            #print(treenode.val) #어떤 값이 출력되는지 테스트용
            
            result.append(treenode.val) # 노드를 맨 윗단부터 탐색, right 탐색 전이므로 1부터 들어간다.
            #해당 문제는 다음 층으로 넘어갈 떄, 탐색을 하는 과정이 재귀의 형태를 띄고있다.
            #그렇기에 역으로 호출할 때도 재귀하는 형태로 호출한다.
            search(treenode.right) #1층 노드 탐색 > 연결된 왼쪽,오른쪽 노드 중 오른쪽만 호출
                                #이 형태를 반복.
                                #더이상 호출할 노드가 없으면 return을 통해 종료한다.
            
        search(root) #전체적인 탐색
        return result #right값만 들어감

