class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        tot = sum(nums)
        div = tot % 3

        # trivial case 
        if div == 0:
            return tot

        tmp1, tmp2, remain1, remain2, full1, full2 = 0, 0, 0, 0, 0, 0
        nums.sort()

        # 전체 합 기준 나머지가 1인지 2인지 판단 후 각기 다르게 진행
        if div == 1:
            remain1 = 1
        else:
            remain2 = 1

        # 나머지 1
        if remain1:
            while not full1 and full2 != 2:
                for n in nums:
                    # 3의 배수이면 안 뺌
                    if n % 3 == 0:
                        continue
                    # 나머지 1일 때 나머지 1인 제일 작은 녀석을 1번만 빼는게 최대값일 확률이 큼
                    if n % 3 == 1 and not full1:
                        full1 = 1
                        tmp1 = n
                    # 나머지 2인 녀석 2번 빼는게 최소값일 수도 있음
                    elif n % 3 == 2 and full2 != 2:
                        full2 += 1
                        tmp2 += n
                break
        # 나머지 2인 경우, 위와 알고리즘 동일
        else:
            print('remain2')
            while full1 != 2 and not full2:
                for n in nums:
                    if n % 3 == 0:
                        continue
                    if n % 3 == 1 and full1 != 2:
                        full1 += 1
                        tmp1 += n
                    elif n % 3 == 2 and not full2:
                        full2 = 1
                        tmp2 = n
                break
        
        tot1, tot2 = tot-tmp1, tot-tmp2
        if tot1 % 3 == 0 and tot2 % 3 == 0:
            return max(tot1, tot2)
        elif tot1 % 3 == 0:
            return tot1
        else:
            return tot2
