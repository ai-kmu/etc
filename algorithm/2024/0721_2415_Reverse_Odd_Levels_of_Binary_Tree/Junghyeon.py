class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = [root]
        
        # flag로 홀/짝 판별
        flag = False
        
        while len(nodes) > 0:
            if flag:
                i = 0
                j = len(nodes) - 1
                while j > i:
                    # 홀수인 경우 서로 값 변경
                    tmp = nodes[i].val
                    nodes[i].val = nodes[j].val
                    nodes[j].val = tmp
                    j -=1
                    i +=1
                    
            tmp_nodes = []
            
            # 자식 노드 추가
            for node in nodes:
                # 완전 이진트리
                if node.left != None:
                    tmp_nodes.append(node.left)
                    tmp_nodes.append(node.right)
        
            nodes = tmp_nodes

            # flag 변경
            if flag:
                flag = False
            else:
                flag = True        
    
        return root
