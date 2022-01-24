#  출제자 comment

#  중위 순회 구현

#  하나씩 방문하여 append를 하는 방식으로 취했다. 
#  원소를 다 추가한 뒤, return answer[k-1]을 이용하여 다 탐색한 뒤에 k번째 작은 수를 호출하였다. -- 1

#  1) 중간에 count를 따로 생성해서 노드를 방문해서 원소를 append를 할 때마다 count를 +1을 하게 만든다. 
#  -> count를 이용하여 정답을 출력하는 방식도 생각해보면 좋을 것 같습니다.

def inorderTraversal(root):
  """
  inorder로 순회하면 정렬된 리스트를 얻을 수 있음.
  
  """
        res = []
        if root:
            res = inorderTraversal(root.left) 
            res.append(root.val)
            res = res + inorderTraversal(root.right)
        return res


      
      
class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        result_list = inorderTraversal(root)
        
        return result_list[k-1]
            
    
