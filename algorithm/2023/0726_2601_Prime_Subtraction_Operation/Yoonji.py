# 559 / 654 testcases passed
# 논리 잘못생각한듯.........................................ㅠㅠ
# nums = [15,20,17,7,16]가 왜 안되는지 모르겠음!!!!ㅠㅠ
import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

class Solution(object):    
    def primeSubOperation(self, nums):
        p=0
        # 길이가 1개면 True
        if len(nums)==1:
            return True

        # 길이가 1개 아닐때 , 모두 같은 숫자일때 ([12,12,12])
        a=set(nums)
        if len(a)==1:
            return False #False

        # 모두 다른 숫자 일때
        else:
            for i in range(len(nums)):
              # 정렬여부 체크
                if (sorted(nums) == nums):
                    # 정렬O True
                    b=set(nums)
                    if len(b)==len(nums):
                        return True  
                    else: #같은 숫자가 있으면 False
                        return False    
                else:
                    #소수 p찾기     
                    for j in range(2, nums[i]):
                        if isPrime(j) == True:
                            p=j
                    nums[i]=nums[i]-p
