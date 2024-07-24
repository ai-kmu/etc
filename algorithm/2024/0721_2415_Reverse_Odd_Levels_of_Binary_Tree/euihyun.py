# 솔루션 참고했습니다

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 현재 레벨의 노드들을 저장하는 리스트
        v = [root] 
        # 현재 레벨 추적
        l = 0  

        while v:
            l += 1
            # 다음 레벨의 노드들을 저장하는 리스트
            vc = []  

            # 현재 레벨의 모든 노드들에 대해 반복
            for i in v:
                if i.left:
                    # 왼쪽 자식이 있으면 다음 레벨 리스트에 추가
                    vc.append(i.left)  
                if i.right:
                    # 오른쪽 자식이 있으면 다음 레벨 리스트에 추가
                    vc.append(i.right) 
                  
            # 현재 레벨이 홀수 레벨인지 확인
            if l % 2 == 1:
                # 홀수 레벨인 경우, 노드의 값을 반전
                for i in range((len(vc) + 1) // 2):
                    vc[i].val, vc[len(vc) - i - 1].val = vc[len(vc) - i - 1].val, vc[i].val

            v = vc  

        return root  
