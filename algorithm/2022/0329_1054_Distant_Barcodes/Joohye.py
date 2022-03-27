'''
# 홀수자리(파이썬 index로는 0,2,4...) 먼저 채워주고, 
# 이후에 짝수자리(파이썬 index로는 1,3,5...)를 채워준다
ex) [1, 1, 1, 1, 2, 2, 2, 3] , 빈도가 제일 높은 수 = 1
    [1, _, 1, _, 1, _, 1, _] , 1 먼저 홀수자리에 채운다
    [1, 2, 1, 2, 1, 2, 1, _] , 홀수자리가 다 찼으니 짝수자리에 2를 채운다
    [1, 2, 1, 2, 1, 2, 1, 3] , 남은 자리에 3을 채운다
'''

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:

        # 각 숫자들의 빈도 확인
        d = {}  # dictionary = d
        for num in barcodes:
            if num not in d:
                d[num] = 0
            d[num] += 1
        
        # 가장 빈도가 많은 수 확인
        maxNum = 0
        maxFreq = 0
        for num in d:
            freq = d[num]
            if freq > maxFreq:
                maxNum = num
                maxFreq = freq
            
        result = [0 for _ in barcodes]  # result 0으로 초기화
        
        # 가장 많은, 빈도 높은 수부터 채워넣기
        idx = 0
        while maxFreq > 0:
            result[idx] = maxNum
            idx += 2  # 홀수자리 먼저 채워야해서 2씩 index 증가
            maxFreq -= 1  # 1 1 1 1 -> 1 1 1
        del d[maxNum]  # 다 채웠으면 지우기
        
        if idx >= len(result):  # 만약 idx가 주어진 범위(홀수자리가 다 찼으면) 를 넘었다면
            idx = 1  # 짝수자리 채우기 시작
        for num in d:
            freq = d[num]
            while freq > 0:
                result[idx] = num
                idx += 2  # 짝수자리만 채워야해서 2씩 index 증가
                freq -= 1  # 2 2 2 -> 2 2
                if idx >= len(result):
                    idx = 1
        return result
                
        
       
