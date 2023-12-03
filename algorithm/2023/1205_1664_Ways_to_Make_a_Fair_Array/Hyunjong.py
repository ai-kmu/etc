# 하다가 답 봤습니다

class Solution(object):
    def waysToMakeFair(self, nums):

        result = 0
        # 홀수 인덱스의 합, 짝수 인덱스의 합, 원래 배열의 홀수 인덱스 값의 합, 원래 배열의 짝수 인덱스 값의 합
        res = [0, 0, sum(nums[::2]), sum(nums[1::2])]

        # 배열을 순회하면서 결과 갱신
        for i in range(len(nums)):
            # 현재 인덱스의 값을 누적하여 더함 (이전 값이 없는 경우는 0)
            res[i % 2] += nums[i - 1] if i > 0 else 0

            # 이전에 저장된 값에서 현재 인덱스의 값을 빼어 누적하여 뺌
            res[2 + i % 2] -= nums[i]

            # 현재까지의 상태에서 배열이 공정한지 확인하고, 공정한 경우 result 증가
            if res[1] + res[3] == res[0] + res[2]:
                result += 1

        return result
