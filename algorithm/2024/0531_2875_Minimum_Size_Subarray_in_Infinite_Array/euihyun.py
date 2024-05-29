# Time limit 나고 정답 봤습니다. 리뷰 안해주셔도 돼요
class Solution(object):
    def minSizeSubarray(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # nums의 길이를 저장
        n = len(nums)

        # 배열의 합이 target을 만족하는 최소 길이를 큰 값으로 초기화
        min_len = float('inf')

        # 현재 윈도우의 합과 윈도우의 시작점을 초기화
        current_sum = 0
        start = 0

        # 윈도우의 끝점을 이동시키며 탐색
        for end in range(2 * n):
            # 무한 배열을 고려하여 실제 값 가져오기
            current_sum += nums[end % n]

            # 현재 합이 target 이상인 경우, 윈도우를 줄여가며 최소 길이를 갱신
            while current_sum >= target:
                # 현재 윈도우의 길이를 계산하여 최소 길이 갱신
                min_len = min(min_len, end - start + 1)

                # 시작점을 한 칸 오른쪽으로 이동시키며 현재 합에서 시작점의 값을 뺌
                current_sum -= nums[start % n]
                start += 1

                # 현재 윈도우 길이가 n을 초과하면 종료 (중복을 피하기 위함)
                if end - start + 1 > n:
                    break

        # 최소 길이가 갱신되지 않은 경우 -1 반환
        return min_len if min_len != float('inf') else -1

                    
