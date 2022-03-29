# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:   
    # 결과 그래프의 노드값을 구하는 부분
    # 순환을 하면서 result값을 계속 더해준다.
    # 맨 위부터 시작하여 탐색을 시작한다.
    def get_sum(self, all_root, target_value, result):
        if all_root.val >= target_value:
            result[0] += all_root.val # 조건을 만족하면 result에 더한다.
        if all_root.left != None:
                # 바라보고 있는 노드의 왼쪽트리 부분에는 모두 해당 노드보다 작은 값만 있다.
                # 따라서 그 부분을 바라보지 않는다.
                if all_root.val != target_value:
                    self.get_sum(all_root.left, target_value, result)
        if all_root.right != None:
            self.get_sum(all_root.right, target_value, result)
        return
    
    # 그래프를 만드는 부분
    # all_root는 전체 원본 트리이다.
    # current_root는 바라보고 있는 노드의 하위 트리이다.
    def make_graph(self, all_root, current_root, result_tree):
        # 왼쪽 부분을 만들자
        if current_root.left != None:
            left_tree = TreeNode()
            result = [0]
            self.get_sum(all_root, current_root.left.val, result) # 왼쪽 노드에 담길 값을 최종적으로 result에 담는다.
            left_tree.val = result[0]
            result_tree.left = left_tree
            self.make_graph(all_root, current_root.left, result_tree.left) # 순환 호출로 이 밑 부분도 만들어나간다.
        
        # 왼쪽과 똑같은 방식으로 오른쪽을 만든다.
        if current_root.right != None:
            right_tree = TreeNode()
            result = [0]
            self.get_sum(all_root, current_root.right.val, result)
            right_tree.val = result[0]
            result_tree.right = right_tree
            self.make_graph(all_root, current_root.right, result_tree.right)
    
    # 결과값으로 TreeNode를 요구하기 때문에
    # TreeNode를 처음부터 만들어나가면서 결과를 만들어나간다.
    def bstToGst(self, root: TreeNode) -> TreeNode:
        result_tree = TreeNode()
        result = [0]
        self.get_sum(root, root.val, result) # 인수로 list를 전달하면 참조 기능을 사용할 수 있다.
        result_tree.val = result[0] # 첫번째 트리를 만들어준다.
        self.make_graph(root, root, result_tree) # 순환을 통해 그래프를 완성해나간다.
        # print(result_tree)
        
        return result_tree
        
