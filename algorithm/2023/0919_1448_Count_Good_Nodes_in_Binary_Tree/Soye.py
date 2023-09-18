# dfs 
# 현재 path의 최댓값을 저장하며 good node의 cnt를 셈

class Solution:
    ans = 0
    def goodNodes(self, root: TreeNode, prevMax = -10001) -> int:
        if root:
            if root.val >= prevMax:
                self.ans +=1
                prevMax = root.val
                print(root.val)
            self.goodNodes(root.left, prevMax)
            self.goodNodes(root.right, prevMax) 
        return self.ans
