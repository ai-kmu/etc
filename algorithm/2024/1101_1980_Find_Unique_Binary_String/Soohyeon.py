class Solution(object):
    def findDifferentBinaryString(self, nums):
        
        binary = []

        # nums안에 있는 문자 하나하나 순회
        for num in nums:
            n = 0
            plus = 0
            # 문자를 10진수로 변환하기 위해 뒤집어줌
            num = num[::-1]
            # 10진수로 변환
            for digit in range(len(num)):
                plus +=  (int(num[digit : digit+1]) * (2 ** digit))
            binary.append(plus)
        
        # 10진수로 표현할수 있는 모든 경우를 비교하여 binary에 없으면 그 숫자를 2진수로 변환하여 return
        for i in range(2 ** len(nums[0])):
            if i not in binary:
                return bin(i)[2:].zfill(len(nums[0]))




    

        
                