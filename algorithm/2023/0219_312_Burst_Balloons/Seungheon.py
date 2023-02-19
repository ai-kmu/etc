
class Solution(object):
    def maxCoins(self, nums):

        # 3개로 로만들수 있는 모든 최대값
        # 4개로 만들 수 있는 모든 최댓값
        # 5개 ...
        #.... 
        # 를 dp를 이용하여 모두 구하는 방식으로 풀이

        nums = [1] + nums + [1]
        dp = [ [0 for _ in range(len(nums))] for _ in range(len(nums))]
        # dp table row
        for i in range(1,len(nums)-1): # 1 2 3 4
            # 시작점의 위치
            for j in range(len(nums)-i-1): # 0 1 2 3 / 1 2 3 / 0 1 / 0
                # 최댓값을 만들기 위해 마지막으로 사용할 값의 idx
                tmp_max = 0
                # 마지막으로 사용할 값중 중간값의 idx
                for k in range(j+1,j+1+i):
                    # 마지막으로 더할값 + k기준 오른쪽을 없엘때 최댓값 + k기준 왼쪽을 없엘때 최댓값
                    # k-j+-1 :  왼쪽 필요한 개수에 해당하는 idx
                    # j+i-k : 오른쪽 필요한 개수에 해당하는 idx
                    tmp_max = max(tmp_max, nums[j]*nums[k]*nums[j+i+1] + dp[k-j-1][j] + dp[j+i-k][k])
                    dp[i][j] = tmp_max

        return dp[-2][0]
