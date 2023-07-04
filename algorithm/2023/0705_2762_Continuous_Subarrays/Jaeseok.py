# 정답 봤습니다(리뷰 x)

from collections import defaultdict

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        answer = 0
        l = 0
        num_dict = defaultdict(int)

        # sliding window 방식으로 풀이
        for r, v in enumerate(nums):
            # right의 값을 딕셔너리에 추가
            num_dict[v] += 1
            # num_dict에 저장된 숫자 중 가장 큰 수와 가장 작은 수의 차가 2 이상이면 left를 움직임
            # 추가적으로 num_dict에 저장된 left가 갖고 있던 숫자를 빼줌
            while max(num_dict.keys()) - min(num_dict.keys()) > 2:
                num_dict[nums[l]] -= 1
                # 이 때, 숫자의 갯수가 0이 되면 딕셔너리에서 삭제
                if num_dict[nums[l]] == 0:
                    num_dict.pop(nums[l])
                # left를 옮겨줌
                l += 1

            # 가능한 subarray를 answer에 더해줌
            answer += (r - l + 1)

        return answer
