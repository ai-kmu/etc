# 1. min 함수 사용 -> 22/51 time limit

from bisect import bisect_left


class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        sum_ = 0
        for i in range(n):
            sum_ += abs(nums1[i] - nums2[i])

        answer = sum_
        for i in range(n):
            cur_diff = abs(nums1[i] - nums2[i])
            new_num = min(nums1, key=lambda x: abs(x - nums2[i]))
            new_sum = sum_ - cur_diff + abs(new_num-nums2[i])
            answer = min(answer, new_sum)

        return answer % (10**9 + 7)


# 2. bisect 사용

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        sum_ = 0
        # 원래 absolute sum을 구할 때의 차를 sum_에 저장
        for i in range(n):
            sum_ += abs(nums1[i] - nums2[i])

        answer = sum_
        # 이분탐색을 하기 위해 nums1을 정렬
        sorted_nums1 = sorted(nums1)
        # 각 절대값의 차를 순회하면서 nums1의 해당 인덱스를 바꿔가며 최적의 차를 찾음
        for i in range(n):
            # 해당 인덱스에서의 원래 차
            cur_diff = abs(nums1[i] - nums2[i])
            # 차의 절대값이 최소가 되려면 nums2의 해당 인덱스에서의 값과 가장 가까운 값을 nums1에서 찾아야 함
            # 이분탐색(bisect_left)를 사용, bisect_left는 찾는 값과 동일한 값이 존재하면 왼쪽으로 둠
            idx = bisect_left(sorted_nums1, nums2[i])
            # 가장 가까운 값은 그 값의 바로 왼쪽(작거나)이거나 바로 오른쪽(큼) 모두 가능함
            # 1. bisect_left의 결과가 가장 왼쪽이 아닌 경우 왼쪽에서 찾아봄
            if idx > 0:
                # 새로운 합은 원래 합에서 현재 인덱스에서의 결과를 뺀 뒤 새로운 결과를 더해줌
                new_sum = sum_ - cur_diff + \
                    abs(sorted_nums1[idx - 1] - nums2[i])
                # answer와 비교하면서 가장 최소가 되는 absolute sum을 찾아감
                answer = min(answer, new_sum)
            # 2. bisect_left의 결과가 가장 오른쪽이 아닌 경우 오른쪽에서 찾아봄
            if idx < n:
                new_sum = sum_ - cur_diff + abs(sorted_nums1[idx] - nums2[i])
                answer = min(answer, new_sum)

        return answer % (10**9 + 7)
