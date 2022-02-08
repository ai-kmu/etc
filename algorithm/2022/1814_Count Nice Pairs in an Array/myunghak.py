# 우리가 구해야 하는것은 nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]) 이다(단 0 < i < j).
# 그러나 대부분의 경우 한쪽 변에는 하나의 변수만 있는것이 좋다.
# 따라서 nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])를 풀자.
# 이 때 만약 nums[i] - rev(nums[i])의 값이 총 n개의 i에 대해 같다면 우리는
# nC2에 대해 풀어야 하므로 n(n-1)/2 를 계산하면 된다.
# 그러나 이 때 속도를 위해 상수인 2는 마지막에 계산하는것이 좋다.
# 즉 ∑(n)(n-1)/2 = (∑(n)(n-1))/2이다. 
# 여기서 n은 nums[i] - rev(nums[i])의 dictionary값이다.

# 추가로 함수내에서 추가적인 변수를 사용하지 않는 경우 lambda 함수를 사용하는 것이 좋다.
# lambda함수는 메모리 절약에 유리하다.

from collections import Counter

class Solution:
    def __init__(self):
        self.countNicePairs = lambda nums: sum(v*(v-1) for v in Counter([int(str(n)[::-1]) - n for n in nums]).values()) // 2 % (10**9+7)
        
# comment : 한 줄에 모두 넣는 것보다는 각 줄별로 한 줄에 하나의 의미를 담는 것이 좋을 것 같음
