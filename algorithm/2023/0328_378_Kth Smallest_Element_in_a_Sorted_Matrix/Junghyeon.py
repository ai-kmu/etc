'''
O(n^2)으로 해결
2차원 matrix를 1차원으로 펼쳐준 다음 정렬 -> k-1 인덱스의 값을 리턴
'''
class Solution(object):
  def kthSmallest(self, matrix, k):
    n = len(matrix)
    flatten_mat = []
    
    for i in range(n):
      for j in range(n):
        flatten_mat.append(matrix[i][j])
    
    flatten_mat.sort()
    
    return flatten_mat[k-1]
