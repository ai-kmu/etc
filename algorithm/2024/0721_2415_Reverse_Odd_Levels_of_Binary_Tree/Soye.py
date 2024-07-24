# 솔루션 참고

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 레벨 별 노드를 저장하기 위한 딕셔너리 생성
        levels = defaultdict(list)
        
        # 재귀 함수 정의: 노드를 순회하면서 레벨을 기록
        def r(n, lev):
            if n is None:
                return
            r(n.left, lev + 1)  # 왼쪽 자식 노드 순회
            r(n.right, lev + 1)  # 오른쪽 자식 노드 순회
            if lev % 2:  # 홀수 레벨일 경우에만 리스트에 추가
                levels[lev].append(n)
        
        r(root, 0)  # 루트 노드에서 시작하여 레벨 0부터 순회
        
        # 홀수 레벨의 노드를 뒤집기
        for lev, arr in levels.items():
            i, j = 0, len(arr) - 1
            while i < j:
                arr[i].val, arr[j].val = arr[j].val, arr[i].val  # 노드 값 교환
                i += 1
                j -= 1
        
        return root  # 수정된 트리의 루트 노드 반환
