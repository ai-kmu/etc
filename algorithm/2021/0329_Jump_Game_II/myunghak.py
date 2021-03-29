# DP 로 품
# ans[-1] = 0으로 시작해
# ans[-2]가 마지막 index까지 갈수 있는거를 저장
# ans[-3]이 ans[-2]를 이용하거나 아니면 바로 갈수 있는것 둘중 작은거 저장
# ans[-4]가 ans[-2]나 ans[-3]을 이용하거나 아니면 바로 갈수 있는것 셋중 작은거 저장
# ....


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = {-1:0}
        for i in range(2, len(nums)+1):

            if -i+nums[-i] >= 0:
                ans[-i] = 1
            elif nums[-i] == 0:
                ans[-i] = 9999999
            else:
                ans[-i] = min([ans[-i+n] for n in range(1,nums[-i]+1)]) +1

        return ans[-len(nums)]
