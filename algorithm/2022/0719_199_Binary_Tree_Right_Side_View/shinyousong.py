# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    lst = [[]]
    def showRightByFloor(self, root, floor): #층별로 오른쪽에서 보기
        if(root.right is not None): self.showRightByFloor(root.right, floor+1)
        if(root.left is not None): self.showRightByFloor(root.left, floor+1)
        while(len(self.lst)-1 < floor): self.lst.append([]) #lst 층 확장
        self.lst[floor].append(root.val)
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(root is None): return [] #아무것도 없는 경우 바로 리턴
        self.lst = [[]]
        self.showRightByFloor(root, 0) #층별로 요소를 오른쪽에서 본대로 추가
        res = []
        for l in self.lst:
            res.append(l[0]) #오른쪽에서 첫번째로 본 것만 추가
        return res

            
