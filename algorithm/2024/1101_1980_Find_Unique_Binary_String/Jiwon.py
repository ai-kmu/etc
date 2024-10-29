class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        depth = len(nums)

        def dfs(node):
            # line 7-8: 종료 조건
            if len(node) == depth:
                if node not in nums:
                    return node
                return None
            
            # 왼쪽 먼저 탐색 후 오른쪽 탐색 진행
            left_node = dfs(node + "0")
            if left_node:
                return left_node
            return dfs(node + "1")

        return dfs("")
