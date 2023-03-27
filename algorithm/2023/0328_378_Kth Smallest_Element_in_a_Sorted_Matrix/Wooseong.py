class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low = matrix[0][0]
        high = matrix[-1][-1]

        # 예외처리: 숫자가 하나만 있을 경우 그게 답임
        if low == high:
            return low

        # 이분탐색
        while low <= high:
            mid = (high - low) // 2 + low
            cnt = 0
            ans = low

            # 각 열에서
            for i in range(n):
                j = n - 1
                # 행을 끝에서부터 탐색
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                # 있을 경우, count 추가
                if j >= 0:
                    cnt += 1 + j
                    ans = max(ans, matrix[i][j])
                # 없을 경우 다음 열로 이동
                else:
                    break

            # 행렬에서의 탐색이 끝나고
            # cnt가 원하는 만큼 차면 그 위치가 정답
            if cnt == k:
                return ans
            # 덜 차면 low를 올림
            elif cnt < k:
                low = mid + 1
            # 넘치면 high를 내림
            else:
                high = mid - 1
        
        # 큰 while을 빠져나오면 low가 답임
        return low

