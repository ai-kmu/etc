#  출제자 comment

#  stack 이용. 

#  스택을 이용하여 잘 풀이한 것 같습니다.
#  재귀를 통해 풀어보는 것도 생각해보면 좋을 것 같습니다.

# 재귀가 아닌 스택을 사용한 풀이
class Solution:
    def kthSmallest(self, root, k):
        stack = [] 
        rank = 0 
        node = root
        
        #while문으로 stack이 빌 때까지 계속 반복
        #처음 들어갈 때 stack이 비어있는 것을 고려하여 node도 조건에 넣음
        while stack or node:
            
            #현재 노드로부터 가장 왼쪽으로 가고, 가는 길마다 노드를 스택에 넣음
            while node:
                stack.append(node)
                node = node.left
                
            #가장 왼쪽에 도달하면 끝에 노드를 pop()으로 꺼낸다
            node = stack.pop()
            
            #기존 순서에서 1을 증가시킨다
            rank += 1
            
            #k가 맞으면 반환
            if rank == k:
                return node.val
            
            #k가 아니면 오른쪽 자식으로 넘어간다. 
            node = node.right
            
            #만약 자식이 없으면 다시 두번째 while문 지나 스택에서 하나 꺼내서 반복 
