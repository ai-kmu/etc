class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # 맥스 값을 확인하고 현재값이 더 크면 정답에 추가
        # 왼쪽 노드 혹은 오른쪽 노드가 있으면 탐색

        answer = 0

        def explore(cur_node, cur_max):
            nonlocal answer

            if cur_node.val >= cur_max:
                answer += 1
                cur_max = cur_node.val

            if cur_node.left:
                explore(cur_node.left, cur_max)
            if cur_node.right:
                explore(cur_node.right, cur_max)

        explore(root, -10**4)

        return answer
