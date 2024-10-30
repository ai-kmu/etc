class Solution(object):
    def findDifferentBinaryString(self, nums):
        # 길이가 1인경우 제외 처리
        if len(nums) == 1:
            if nums[0] == "1":
                return "0"
            else:
                return "1"
        # 십진수로 변환
        tmp = []
        for i in nums:
            tmp_len = len(i)
            tmp_val = 0
            for j in i:
                tmp_val += int(j) * (2 ** (tmp_len-1))
                tmp_len -= 1
            tmp.append(tmp_val)
        
        # max 숫자를 십진수로 계산
        len_n = len(nums)
        max_val = 0
        for i in range(len_n):
            max_val += 2**i
        
        # 십진수로 정답값 찾기
        for i in range(1, max_val+1):
            if i not in tmp:
                aws = i
                break
        
        # 십진수를 이진수로 변환
        bi=""
        while aws !=0:
            if aws%2==0:
                bi="0"+bi
                aws=aws//2
            else:
                bi="1"+bi
                aws=aws//2

        # 문자열 크기 맞춰주기
        if len(bi) != len(nums):
            k = len(nums) - len(bi)
            bi = k * '0' + bi
        return bi
