class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # tree 형태라고 생각하고 품
        # root node(0)에서 시작해서 값을 바꿔가는 방식
      
        # leaf 시작점과 끝점
        leaf_start = 1
        leaf_end = 2 ** (n - 1)

        # 현재 val값
        cur_num = 0

        for _ in range(n-1):
            # k가 더 크면 오른쪽
            if (leaf_end + leaf_start) // 2 < k:
                cur_num = 1 if cur_num == 0 else 0 
                leaf_start = (leaf_end + leaf_start) // 2 + 1     
            # k가 같거나 작으면 왼쪽
            else:
                leaf_end = (leaf_end + leaf_start) // 2
              
        return cur_num
