class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # O(n^2)로 풀면 시간 에러남
        # O(n) 코드
        
        # max_score: 최대 score
        # 초기 값은 values의 0번째와 1번째에서만 계산
        max_score = values[0] + values[1] - 1
        
        # trivial case
        if len(values) == 2:
            return max_score
        
        # values를 순회하면서 val을 활용해 max_score를 갱신할 수 있는지 판단한다
        # 여기서 max_val 값을 저장해놓고 있으면, 모든 값을 다 볼 필요가 없다
        # 중요한 점은 거리도 고려해야 하므로 0번째 값에는 2만큼, 1번째 값은 1만큼 뺀다
        max_val = max(values[0] - 2, values[1] - 1)
        
        for val in values[2:]:
            new_score = val + max_val
            if new_score > max_score:
                max_score = new_score
            
            if val > max_val:
                max_val = val
            # 순회할수록 거리가 멀어지므로 1만큼 빼야함
            max_val -= 1
            
        return max_score
        
