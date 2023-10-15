from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        # nums의 개수만큼 k개가 떨어지지 않으면 False
        if l % k != 0:
            return False

        num_count = Counter(nums)
        
        # 떨어지는 경우 순회는 l을 k개로 나눈 것만큼 계속 list를 나눠줌
        for i in range(l // k):
            # 현재 가장 작은 숫자를 뽑고
            min_num = min(num_count)
            for i in range(k):
                # 그 숫자 이후의 순서의 숫자가 없으면 False
                if num_count[min_num + i] == 0:
                    return False
                # 있다면 그 숫자의 갯수를 하나 줄여줌
                num_count[min_num + i] -= 1
                # 만약에 그 숫자를 전부 다 썼다면 Counter에서 지워줌
                if num_count[min_num + i] == 0:
                    del num_count[min_num + i]
        # 순회를 다 돌 돌았다면 무조건 True
        else:
            return True
