class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        answer = []
        
        def BFS(root):
            if root:
                # BFS를 활용해서 왼쪽노드를 탐색하고 이진 탐색 트리이기 때문에 왼쪽에 있는 노드가 더 작다.
                # 따라서 answer에 append를 해준다.
                BFS(root.left)
                answer.append(root.val)
                # 루트 노드의 오른쪽 노드도 탐색을 한다.
                BFS(root.right)
            
        BFS(root)
        # k번째 작은 노드를 반환해야하기 때문에 k-1인덱스를 return해준다.
        return answer[k-1]

   #하나씩 방문하여 append를 하는 방식으로 취했다. 1
   #return answer[k-1]을 이용하여 다 탐색한 뒤에 k번째 작은 수를 호출하였다. 중간에 count를 따로 생성해서 count가 k와 같으면 break를 하는 방식을 고려하면 좋겠다. 1
