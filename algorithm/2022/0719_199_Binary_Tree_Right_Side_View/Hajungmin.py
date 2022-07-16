from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 만일 root가 없으면 그대로 return
        if not root:
            return 
        
        # 레벨 탐색을 위해 deque사용
        # 현재 레벨과 root값 넣어줌
        q = deque()
        q.append((0, root))
        res = []
        tmp = 0
        
        while q:
            level, value = q.popleft()
            
            # 만약 현재 root의 오른쪽에 값이 있다면
            # 오른쪽 값의 레벨과 root값 deque에 append
            # 왼쪽도 마찬가지
            if value.right:
                q.append((level+1, value.right))
            
            if value.left:
                q.append((level+1, value.left))
            
            # 만약 현재 tmp값과 deque에서 나온 level이 일치하다면 
            # 결과에 append한 후 tmp + 1
            # 각 레벨마다 deque에서 나오는 첫 번째 수는 가장 오른쪽 수
            if level == tmp:
                res.append(value.val)
                tmp += 1
        
        return res
