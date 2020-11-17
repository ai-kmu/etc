#Binary_Tree_Inorder_Traversal
# 11:35~11:51
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):

        #방문한 노드 저장
        answer=[]
        self.traversal(root,answer)

        return answer

    #실제 inorder traversal 코드
    def traversal(self,root,answer):

        if root==None: # 아예 노드가 없는 경우
            return answer
        if root.left != None: # inorder traversal니까 재귀 호출
            self.traversal(root.left, answer)
        answer.append(root.val) # 왼쪽 다 돌았으면 중간 노드 넣어주기
        if root.right != None: # 오른쪽 순회 
            self.traversal(root.right, answer)
            return answer

        return answer



if __name__ == '__main__':
    # mainTree=TreeNode(1)
    # tree1=TreeNode(2)
    # tree2=TreeNode(3)
    # tree1.left=tree2
    # mainTree.right=tree1()



    s=Solution()
    print(s.inorderTraversal(None))