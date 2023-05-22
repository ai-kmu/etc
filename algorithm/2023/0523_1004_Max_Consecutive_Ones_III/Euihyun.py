# 솔루션 보고 풀었습니다 리뷰 안해주셔도 돼요.

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0  
        # 윈도우 내의 0의 개수
        zeros = 0  
        max_length = 0 

        for right in range(len(nums)):
            # 현재 요소가 0인 경우 0의 개수를 증가시킴
            if nums[right] == 0:
                zeros += 1

            # 윈도우 내의 0의 개수가 K를 초과하면
            # 윈도우의 왼쪽을 이동시키고 0의 개수를 감소시킴
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            # 현재 윈도우의 길이가 최대 길이보다 크면 갱신
            max_length = max(max_length, right - left + 1)

        return max_length
