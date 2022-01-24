#  출제자 comment

#  중위 순회 구현
#  counter를 사용한 것이 독특한 것 같습니다.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    counter = 0
    result = None
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.counter = 0
        self.result = None
        
        self.traverse(root,k)
        
        return self.result
    
        
    #Inorder Traversal, 중위순회를 사용하여 결과를 도출했다.
    #중위순회란 left child - self - right child 순으로 탐색을 하는 것이다.
    #이 순서로 탐색을 하면 저절로 정렬된 값을 얻을 수 있다.
    #함수는 재귀적 방법을 사용하였다.
    
    def traverse(self, root, k):
        if root == None:
            return
        
        #left child가 있을 경우 함수를 불러옴
        self.traverse(root.left, k)
        
        self.counter += 1
        
        if self.counter == k:
            
            self.result = root.val
        
        #right child가 있을 경우 함수를 불러옴
        self.traverse(root.right, k)
        

"""
두번째 예시를 보면

  5에서 left child가 있으니까 traverse 함수를 불러오고
  
  3에서 left child가 있으니까 traverse 함수를 불러오고
  
  2에서 left child가 있으니까 traverse 함수를 불러오고
  
  1에서는 left child가 없어서 count += 1을 수행, right child도 없으니 마지막으로 불러온 함수 탈출
  다시 2로 돌아와서 방금 self.traverse(root.left, k) 함수를 빠져나왔으니 바로 count +1
  
  그후 2에 right child가 없으니 함수 탈출
  
  3으로 돌아와서 count +1 하면 count = 3이 되고 이는 k 값과 같아지면서 해당하는 root.val인 3을 return한다.
  """
  
