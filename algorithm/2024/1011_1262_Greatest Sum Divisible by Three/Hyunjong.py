class Solution(object):
    def maxSumDivThree(self, nums):
        # 경우의 수가 3개 (x % 3 == 0, x % 3 == 1, x % 3 == 2)
        zero = 0
        one = 0
        two = 0

        # nums 개수만큼 돌면서 최대값 update
        for i in nums:
            # 임시 저장용
            zero_tmp = zero
            one_tmp = one
            two_tmp = two

            # 새로운 값 i를 기존 값에 더한 후 갱신
            
            # zero에서 새로운 값 i를 더한 경우
            if (i + zero_tmp) % 3 == 0:
                zero = max(zero, i + zero_tmp)
            elif (i + zero_tmp) % 3 == 1:
                one = max(one, i + zero_tmp)
            else:
                two = max(two, i + zero_tmp)

            # one에서 새로운 값 i를 더한 경우
            if (i + one_tmp) % 3 == 0:
                zero = max(zero, i + one_tmp)
            elif (i + one_tmp) % 3 == 1:
                one = max(one, i + one_tmp)
            else:
                two = max(two, i + one_tmp)

            # two에서 새로운 값 i를 더한 경우
            if (i + two_tmp) % 3 == 0:
                zero = max(zero, i + two_tmp)
            elif (i + two_tmp) % 3 == 1:
                one = max(one, i + two_tmp)
            else:
                two = max(two, i + two_tmp)

        # 3으로 나누어 떨어지는 최대 합을 반환
        return zero
