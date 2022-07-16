class Solution(object):
    def rightSideView(self, root):
        
        # 예외처리
        if not root:
            return []
        
        answer = [101 for _ in range(101)]
        
        # 최대 노드 측정을위함
        max_layer = 0
        
        # 오른쪽 먼저 탐색후 왼쪽 탐색, 탐색한 layer는 탐색하지 않음
        def explore(node, layer):
            nonlocal answer
            nonlocal max_layer
            
            max_layer = max(max_layer, layer)
            # 방문하지 않았으면
            if answer[layer] == 101:
                answer[layer] = node.val
            if node.right:
                explore(node.right, layer+1)
            if node.left:
                explore(node.left, layer+1)
            return 
        
        explore(root, 0)
        
        return answer[:max_layer+1]
