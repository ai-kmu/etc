#  출제자 comment

#  중위 순회 구현

#  하나씩 방문하여 append를 하는 방식으로 취했다. 
#  원소를 다 추가한 뒤, return answer[k-1]을 이용하여 다 탐색한 뒤에 k번째 작은 수를 호출하였다. -- 1

#  1) 중간에 count를 따로 생성해서 노드를 방문해서 원소를 append를 할 때마다 count를 +1을 하게 만든다. 
#  -> count를 이용하여 정답을 출력하는 방식도 생각해보면 좋을 것 같습니다.


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
## BST는 왼쪽 트리값 < root값 < 오른쪽 트리값 으로 구성되어 있다
## 중위 탐색(left -> root -> right)을 하면 정렬된 순서로 만들 수 있다
## recursive한 방법

        ans = []
        self.inorder(root, ans)
        return ans[k-1]
    
    def inorder(self, root, ans):
        ## root를 전부 탐색했으면 return ans
        if not root:
            return ans

        ## 탐색할 root가 남은 경우
        ## 왼쪽 탐색
        if root.left:
            self.inorder(root.left, ans)
        
        ## root 저장
        ans.append(root.val)
        
        ## 오른쪽 탐색
        if root.right:
            self.inorder(root.right, ans)
