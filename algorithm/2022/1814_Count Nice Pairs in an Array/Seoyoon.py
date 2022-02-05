# (nums[i] - rev(nums[i])) == (nums[j] - rev(nums[j])) 이렇게 되는 쌍을 찾고싶은 문제

class Solution:
    def countNicePairs(self, nums):

        ## hashmap(dict)를 만듦
        d = {}
        
        ## nums의 num을 반복하면서 뒤집은 수와의 차이 계산해서 gain에 저장
        for num in nums:
            gain = int(str(num)[::-1]) - num
            
            if not (gain in d): 
                d[gain] = 1 #만약 gain이 d 에 없으면 1
            else:
                d[gain] += 1 # dictionary에 있는 gain에 1 증가
            
        ## hashmap(dict)에서 nice pair 계산
        num_of_nice_pairs = 0 # 초기값 0으로 지정
        for gain in d:
            n = d[gain] # n은 같은 gain을 가지는 숫자의 요소를 의미 
            if n >= 2:
                num_of_nice_pairs +=  (n*(n-1))//2 #nC2 계산
        
        ## 숫자가 너무 클 경우 modulo 반환
        return num_of_nice_pairs % (10**9 + 7)
