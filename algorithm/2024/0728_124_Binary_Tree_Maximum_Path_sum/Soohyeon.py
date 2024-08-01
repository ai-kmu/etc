# 솔루션 참조
# https://m.blog.naver.com/qbxlvnf11/222905099266
class Solution(object):
    def maxPathSum(self, root):
        # 초기 설정(합의 결과값)
        self.res = -1000
        # dfs 방식으로 접근 -> 위에서 아래로 접근
        def dfs(root):
            if not root: 
                return 0
            # 왼쪽,오른쪽 노드로 들어가서 뿌리인지 아닌지 확인하고 만약 뿌리라면 값을 비교
            # 만약 뿌리가 아니라면 dfs 다시 루프
            # 예외적으로 전부가 -일 경우는 코드가 돌아가지 않을 가능성이 있음.. (0보다 작으면 더해주지 X)
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            # 현재 값과 저장된 값을 비교하여 비교후 설정
            self.res = max(self.res, root.val + left + right)

            return root.val + max(left, right)
        dfs(root)
        return self.res