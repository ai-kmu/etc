class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
            zeros = 0 # 0의 개수 
            l = 0 # 왼쪽 인덱스 값

            '''         
            <슬라이딩 윈도우 방법으로 풀이>
            오른쪽 인덱스 값 r이 오른쪽으로 이동하면서
            nums[r]이 0이면 zeros += 1.
            그러다가 어느 순간 zeros가 k보다 커지면
            일단 무조건 왼쪽 인덱스 l을 1 증가시킴.
            그리고 zeros가 k보다 클 때
            왼쪽 인덱스 l 위치의 nums값이 0인 경우
            zeros -= 1.
            이런 방식으로 l,r 값을 이동시켜서
            마지막까지 for문을 돈 후
            r-l+1이 최종 정답값.
            '''
            for r,v in enumerate(nums):
                if nums[r] == 0:
                    zeros += 1 
                if zeros > k:
                    if nums[l] == 0:
                        zeros -= 1 
                    l += 1
            return r-l+1
