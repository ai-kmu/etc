## 풀이 방식
## Tree 구조(이진 Tree) => 좌측은 작은 값 / 우측은 큰 값 할당 / 가장 우측 노드부터 값을 불러와서 더함

class Solution:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.sum_val = 0
    
    def bstToGst(self, tree):
        
        # tree에 있는 Node값이 None이 아닌 경우
        if tree != None:
        
        # (1) Tree right node의 None아닐 경우 오른쪽을 탐사
            if tree.right != None:
                self.bstToGst(tree.right)
        
        # (2) 오른쪽 값(가장 큰 값) 부터 sum_val에 저장함
            tree.val = tree.val + self.sum_val
           
        # (3) 그값을 다시 할당
            self.sum_val = tree.val
        
        # (4) 이후 left node의 값이 None이 아닐경우 이어서 오른쪽 Node의 값을 더한값을 차례로 더해 할당
            if tree.left != None:
                self.bstToGst(tree.left)
        return tree
        
        
        
# 개인 풀이 내용(Tree가 아니라 list로 주어졌을때)---------------- 
(이부분은 Tree 구조 dictionary 저장 안되었을 떄 / list로 주어졌을 때 가정하고 풀어봤습니다. / 코드 review 안하셔도 됩니다.)

def bstToGst(root):
    
    # 각 노드 값을 sorting(내림차순)
    only_list = sorted([value  for value in root if value != None], reverse = True)
    
    # 각각 sum한 list 생성
    cnt_sum = []
    for index, sum_value in enumerate(only_list):
        cnt_sum.append(sum_value) if sum_value == only_list[0] else cnt_sum.append(cnt_sum[index - 1] + sum_value)
    
    # node 값과 대응되는 sum 값을 diectionary 형태로 저장
    corr = {}
    corr[None] = None
    
    # 각 위치에 맞게 할당
    for i in range(len(only_list)):
        corr[only_list[i]] = cnt_sum[i]

    result = []
    for key in root:
        result.append(corr[key])
    
    return result
