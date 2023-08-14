# 테케 실패후 정답 봤어요 리뷰 안해주셔도 됩니다.
class Solution(object):
    def minIncrements(self, n, cost):
        ans = 0
        # 각 레벨에서의 최대 비용을 저장할 리스트 생성
        sums = [0] * (n // 2)  
        # 레벨 역순으로 탐색    
        for i in range(n - 1, 1, -2):  
            # 현재 노드의 왼쪽과 오른쪽 자식 노드 비용
            left_sum, right_sum = cost[i - 1], cost[i]  
            # 왼쪽 자식의 하위 경로 비용 추가
            # 오른쪽 자식의 하위 경로 비용 추가
            if i < len(sums):
                left_sum += sums[i - 1]  
                right_sum += sums[i]     
            # 현재 노드의 부모 노드로 경로 비용 업데이트
            sums[i // 2 - 1] = max(left_sum, right_sum)
            # 추가된 비용을 결과에 더함
            ans += sums[i // 2 - 1] - min(left_sum, right_sum)  

        return ans
