class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        queue = collections.deque([root])
        
        while queue:
            rightside = None
            qlen = len(queue)
            
            for _ in range(qlen):
                node = queue.popleft()
                if node:
                    rightside = node
                    queue.append(node.left)
                    queue.append(node.right)
                    
            if rightside:
                answer.append(rightside.val)
                
        return answer
