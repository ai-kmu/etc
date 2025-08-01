# 풀다가 솔루션 봤습니다. 풀이 안해주셔도 됩니다.

class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7  
        
        n = len(nums)
        freq = [0] * (n + 1)  

        # request에 대해 시작점에 +1, 다음 인덱스에 -1
        # end가 포함되므로 end+1에 빼줌
        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1  

        # 각 위치의 포함 횟수를 계산
        for i in range(1, n):
            freq[i] += freq[i - 1]
        freq = freq[:n]  

        # 자주 쓰인 인덱스에 가장 큰 nums 값을 배치해야 하므로 둘 다 정렬
        freq.sort()      
        nums.sort()      

        # 자주 쓰이는 위치에 큰 수를 곱해서 최대화
        total = 0
        for f, num in zip(freq, nums):
            total = (total + f * num) % MOD

        return total
