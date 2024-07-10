from collections import deque

class Solution:
    def is_inbound(val, max):
      return val >= 0 and val < max

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
      if not mat or not mat[0]:
          return []
      
      h, w = len(mat), len(mat[0])
      x, y = 0, 0
      starting_x = 0
      diagonal_list = []

      # w, h중 더 큰 값
      max_size = max(w, h)

      is_inversed = False
      for i in range(h + w - 1):
        deq = deque()

        if i < w: # x축을 벗어나지 않았다면
          x_pos, y_pos = 0, i
        else: # x축을 벗어났다면
          x_pos, y_pos = i - w + 1, w - 1

        while Solution.is_inbound(x_pos, h) and Solution.is_inbound(y_pos, w):
          if is_inversed:
            deq.append(mat[x_pos][y_pos])
          else:
            deq.appendleft(mat[x_pos][y_pos])

          x_pos += 1
          y_pos -= 1
              
        # deq to list
        deq = list(deq)

        # 하나의 list로 합치기
        diagonal_list.extend(deq)
        starting_x += 1
        is_inversed = not is_inversed

      return diagonal_list
