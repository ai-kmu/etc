import math 

class Solution:
    def find132pattern(self, nums):  
        rightMiddle = -math.inf
        s = list()
        for n in nums[::-1]:  # 리스트 뒤집기
            if n < rightMiddle: # i < j < k 인지 검사
                return True
            while s and s[-1] < n:  # n을 중심으로 right에 있는 값 중 가장 큰 값 rightMiddle에 저장
                rightMiddle = s.pop()
            s.append(n)
        return False   
