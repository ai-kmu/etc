class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 초기값 선언
        self.good =0
        # dfs로 풀이
        def dfs(node: TreeNode, curMax) :
            # node 비어있으면 아무것도 리턴 안함
            if not(node): return 
            # 조건 충족하면 +1, curMax 업데이트해줌
            if (node.val>=curMax): 
                self.good += 1
                curMax = node.val

            dfs(node.left,curMax)
            dfs(node.right,curMax)

        dfs(root,-sys.maxsize-1)
        return self.good
