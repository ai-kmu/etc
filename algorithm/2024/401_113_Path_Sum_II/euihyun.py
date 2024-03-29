# 그래프는 아예 못하겠네요,, 정답 봤습니다. 리뷰안해주셔도 돼요

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ans = []  # 결과를 저장할 리스트

        # 트리를 순회하면서 경로의 합이 목표 합(targetSum)과 같은 경로를 찾는 재귀 함수
        def tree_traversal(root, curr_sum, curr_path):
            # 현재 합에 현재 노드의 값을 추가
            curr_sum += root.val  
            # 현재 경로에 현재 노드의 값을 추가
            curr_path.append(root.val) 

            # 만약 현재 노드가 말단 노드인 경우(자식 노드가 없는 경우)
            if root.left == None  and root.right == None:
                # 현재 합이 목표 합과 같으면 결과 리스트에 현재 경로 추가
                if curr_sum == targetSum:
                    ans.append(curr_path)
                return  
            
            # 왼쪽 자식이 있는 경우, 왼쪽 자식으로 재귀 호출
            if root.left:
                tree_traversal(root.left, curr_sum, list(curr_path))
            
            # 오른쪽 자식이 있는 경우, 오른쪽 자식으로 재귀 호출
            if root.right:
                tree_traversal(root.right, curr_sum, list(curr_path))

        if root: 
            # 트리 순회 함수 호출, 현재 합과 경로는 0으로 초기화
            tree_traversal(root, 0, [])
        return ans  # 결과 리스트 반환
