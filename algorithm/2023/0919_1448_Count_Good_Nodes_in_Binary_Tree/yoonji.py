class Solution:
    def goodNodes(self, root):
        def dfs(root, prevMax, count):
            # 만약 현재 노드의 값(root.val)이 이전까지의 최댓값(prevMax)보다 크거나 같으면,
            if root.val >= prevMax:  
                # 현재 노드를 "좋은 노드"로 간주하고 count를 1 증가
                prevMax = root.val  
                count+=1    

            # 왼쪽 서브트리가 존재하면 왼쪽 서브트리에서 dfs를 재귀적으로 호출하고 count를 업데이트
            if root.left:     
                count = dfs(root.left, prevMax, count)   
            # 오른쪽 서브트리가 존재하면 오른쪽 서브트리에서 dfs를 재귀적으로 호출하고 count를 업데이트
            if root.right:
                count = dfs(root.right, prevMax, count)
            
            return count
            # dfs 함수를 최초 호출하고, 최초의 prevMax를 현재 루트 노드의 값(root.val)으로 설정하고 count를 0으로 초기화
        return dfs(root, root.val, 0)
