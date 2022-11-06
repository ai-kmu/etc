# Memory Limit...

# 1개, 1개, 1개, 1개 케이스를 생각하면 결국 조합을 써야됨
# 중복조합을 쓰는 것이 낫긴 할 것 같은데 너무 크다
# 조합을 한번 도는것 자체가 아까우니 정렬된 값을 조합으로 만들어서 약간 정렬되어있게 해놓자
# [-200, -200, -200, -200], [-200, -200, -200, -199], ... [-199, -199, -199, -199], ... [-1, -1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 0]
# 이러면 앞뒤로 불가능한 그룹 몇개를 날려버릴 수 있다.

from collections import defaultdict
import itertools
class Solution:
    def fourSum(self, nums, target):
        # 중복조합 공식을 위한 factorial
        def factorial(nums):
            if nums == 0:
                return 1
            cnt = 1
            for i in range(1, nums+1):
                cnt *= i
            return cnt

        # 리스트에 숫자가 몇개씩 있는지 나타내는 사전 생성
        dic = defaultdict(int)
        for item in nums:
            dic[item] += 1

        # 첫과 끝의 값의 합이 target 만들기를 불가능하게 하는 경우 그만큼 자른다.
        # 불가능한 경우를 리턴한다   
        nums = sorted(list(set(nums)))
        res = []
        if (target > nums[-1]*4 or target < nums[0]*4):
            print(nums[-1]*4, nums[0]*4)
            return res

        # 메모리가 터져서 중복조합을 인덱스로 하여 자료형을 줄이는 시도
        # 그래도 양이 많아서 안된다
        # 중복순열 생성 전에 불가능한 가짓수를 쳐내기를 요구?
        temp = list(itertools.combinations_with_replacement([i for i in range(len(nums))], 4))
        # temp = list(itertools.combinations_with_replacement(nums, 4))

        # 크게 한번 범위 잡기
        idx_front = 0
        idx_last = len(temp) - 1
        len_data = len(nums)
        len_last_data = 1
        while (idx_front < len(temp)):
            # 최댓값 3배+최소가 타겟보다 작은 동안
            if target > nums[-1]*3 + nums[temp[idx_front][0]]:
                # 중복조합 공식
                idx_front += int(factorial(len_data+3-1)/factorial(len_data-1)/factorial(3))
                len_data -= 1
            else:
                break
        while (idx_last > 0):
            # 최솟값 4배가 타겟보다 큰 동안
            if nums[temp[idx_last][0]]*4 > target:
                # 중복조합 공식
                idx_last -= int(factorial(len_last_data+3-1)/factorial(len_last_data-1)/factorial(3))
                len_last_data += 1
            else:
                break
        # 이젠 세부적인 단계별로 걸러주자, 순방향으로만
        idx = idx_front
        t = idx_front
        flag = 1
        len_subdata = len_data
        while (idx <= idx_last):
            # len_data는 threshold가 넘으면 업데이트
            if t == idx:
                t += int(factorial(len_data+3-1)/factorial(len_data-1)/factorial(3))
                len_subdata = len_data
                len_data -= 1
                flag = 1
                continue
            # 최댓값 2배+앞 두개의 합이 타겟보다 작으면 그만큼 건너뜀
            if flag and target > nums[-1]*2 + nums[temp[idx][0]]+nums[temp[idx][1]]:
                # 중복조합 공식
                idx += int(factorial(len_subdata+2-1)/factorial(len_subdata-1)/factorial(2))
                len_subdata -= 1
                continue
            else:
                flag = 0
            temp_sub = [nums[temp[idx][i]] for i in range(4)]
            if (sum(temp_sub) == target):
                # 양이 되나 체크
                tempdict = defaultdict(int)
                flag = 1
                for item in temp_sub:
                    tempdict[item] += 1
                for item in tempdict:
                    if dic[item] < tempdict[item]:
                        flag = 0
                if flag:
                    res.append([temp_sub[j] for j in range(4)])
            idx += 1
        return res
