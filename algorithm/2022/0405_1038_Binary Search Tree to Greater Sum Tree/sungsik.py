# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from itertools import accumulate


class Solution:
    # inorder search를 통해 tree를 크기 순으로 정렬
    def inorderSearch(self, root, tree):
        if root == None:
            return
        self.inorderSearch(root.left, tree)
        tree.append(root.val)
        self.inorderSearch(root.right, tree)
        return tree
    
    # inorder 순서에 따라
    # cumulative sum을 수행한 tree의 값으로 할당
    def inorderAssign(self, root, cumsum_tree):
        if root == None:
            return cumsum_tree
        cumsum_tree = self.inorderAssign(root.left, cumsum_tree)
        val = cumsum_tree[0]
        cumsum_tree = cumsum_tree[1:]
        root.val = val
        cumsum_tree = self.inorderAssign(root.right, cumsum_tree)
        return cumsum_tree
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 크기 순으로 정렬 후 역순으로 바꿈
        tree = self.inorderSearch(root, [])[::-1]
        # cumulative sum을 진행한 후 다시 역순으로 바꿈
        # itertools.accumulate => numpy.cumsum과 비슷한 함수
        cumsum_tree = list(accumulate(tree))[::-1]
        # 다시 크기 순서대로 cumulative sum한 결과를 할당함
        self.inorderAssign(root, cumsum_tree)
        return root
