from collections import defaultdict
class Solution:
    
#sub matrix의 누적을 이용.

    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """
        res = 0
        row,col = len(matrix),len(matrix[0])
        for k in range(row):
            nums = [0 for _ in range(col)]
            for i in range(k,row):
                #밑으로 내려가면서 같은 column끼리 sum 누적
                for j in range(col):
                    nums[j] += matrix[i][j]
                res += self.check(nums,target)
        return res
    
    def check(self,nums,target):
        counter,res = defaultdict(int),0
        counter[0],cum_sum = 1,0
        for num in nums:
            cum_sum += num
            #cum_sum - target 있다는 것은 sub mat이 같다는 것.  column의 누적을 이용
            res += counter[cum_sum - target]
            counter[cum_sum] += 1
        return res

    
#     def equal_target(self, mat , r, c, target):
#         answer = 0
#         for i in range(len(mat)-r+1):
#             mat_sum = []
#             for j in range(len(mat[i])-c+1):
#                 mat_sum = sum([sum(mat[r_i][j:j+c]) for r_i in range(i, i+r)])
#                 if mat_sum == target:
#                     answer += 1
#         return answer
    
#     def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
#         answer = 0
#         R, C = len(matrix), len(matrix[0])
#         # 모든 element의 합이 target이 되는 sub matrix 만들기

#         for r in range(R):
#             for c in range(C):
#                 answer += self.equal_target(matrix , r+1, c+1, target)
#         return answer

