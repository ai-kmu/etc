from collections import Counter


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        '''
        배열의 길이 10^5 -> brute force로 풀이시 Time Limit Exceeded발생
        i + rev(j) == rev(i) + j --->>> i - rev(i) = j - rev(j)
        즉, num - rev(num)의 결과가 같은 수들끼리 묶어서 해결한다.
        1. 각각의 수들에서 rev한 값을 뺀것들을 저장한 리스트를 만든다.
        2. Counter를 이용해서 빈도를 계산한다.
        3. Combination을 이용해서 모든 경우의수를 더해준다.
        '''
        cnt = 0
        num_sub_list = list()
        # 값이 너무 커지는 것을 막기 위해 MOD사용
        # MOD 없이도 Colab에서는 올바른 값이 나오지만 LeetCode에서는 틀린 값이 나오는 이유...?
        MOD = 10**9 + 7
        
        # num - rev(num)의 결과값들을 리스트에 저장
        for num in nums:
            num_sub_list.append(num - int(str(num)[::-1]))
        
        # n = 빈도수    
        # Counter를 이용해서 각각의 수들의 빈도를 계산하고 C(n, 2)를 한 값을 cnt에 더해준다.     
        for n in Counter(num_sub_list).values():
            cnt += (n * (n-1) // 2)
            
        return cnt % MOD
