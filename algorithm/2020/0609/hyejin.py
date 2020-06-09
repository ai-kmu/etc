from collections import deque
class Solution:
    
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 방문을 하면서 반대로 뒤집어준다.
        # queue를 이용하여 풀음.
        queue = deque()
        queue.append(root)
        while queue:
            # queue에서 첫번째 node를 뽑음
            node = queue.popleft()
            # 그 노드가 Nond일 경우를 체크함.
            if node:
                # left와 right를 반대로 뒤집어 줌. 
                #트리는 밑으로 내려가면서 뒤집어진다.
                node.right, node.left = node.left, node.right
                queue.append(node.left)
                queue.append(node.right)
        return root
