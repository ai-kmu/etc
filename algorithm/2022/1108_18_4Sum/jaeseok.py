class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        # 리스트를 정렬하여 비교해 가면서 정답을 탐색
        nums.sort()
        n = len(nums)
        # 양 끝에다 포인터를 지정
        for i in range(0, n):
            for j in range(n-1, i, -1):
                # i와 j 사이에서 k와 l이 이동함
                # 합이 target보다 작으면 k를 늘려주고, 작으면 l을 줄여줌
                k = i + 1
                l = j - 1
                # k가 l과 같아져서 더 이상 연산이 의미가 없어질때까지 수행
                while k < l:
                    sum_ = nums[i] + nums[j] + nums[k] + nums[l]
                    # 중복을 허용하지 않으면서 target값과 같은 sum을 output에 추가
                    if sum_ == target and [nums[i], nums[j], nums[k], nums[l]] not in output:
                        output.append([nums[i], nums[j], nums[k], nums[l]])
                        # 없어도 되지만 if문을 한번 더 수행하는 것을 방지
                        k -= 1
                    # 합이 target보다 작으면 k를 늘려 sum_을 키워줌
                    elif sum_ < target:
                        k += 1
                    # 합이 target보다 크면 l을 줄여 sum_을 줄여줌
                    else:
                        l -= 1

        return output
