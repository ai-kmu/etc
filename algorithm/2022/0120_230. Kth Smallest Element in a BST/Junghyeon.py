# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        문제풀이 방법
        BST의 경우, 항상 leftnode < rootnode < rightnode가 성립한다.
        즉, Inorder방식(left -> root -> right)으로 tree를 순회하고 해당 인덱스에 해당하는 값을 저장한다.
        DFS(Depth First Search)를 이용해서 tree 탐색
        '''
        answer = list()
        
        # 재귀를 이용해서 DFS구현
        def DFS(node):
            # 노드가 비어있지 않다면
            if node:
                # 왼쪽 노드 탐색
                DFS(node.left)
                # 현재 위치의 노드를 리스트에 저장
                answer.append(node.val)
                # 오른쪽 노드 탐색
                DFS(node.right)
        
        DFS(root)
        
        # if k가 i일 경우, i-1번째 idx를 리턴해야함(리스트의 idx는 0부터 시작)  
        return answer[k-1]
