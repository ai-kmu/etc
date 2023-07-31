# test만 풀고 정답 봤습니다.
# 리뷰 안해주셔도 됩니다.
class Solution(object):
    def combinationSum(self, candidates, target):
        # 조합 결과를 저장할 리스트
        ret = [] 
        # 깊이 우선 탐색을 통해 조합 결과를 구함.
        self.dfs(candidates, target, [], ret) 
        return ret
    
    def dfs(self, nums, target, path, ret):
        # 목표 합을 초과하면 해당 조합은 유효하지 않음ㅍ
        if target < 0: 
            return 
        # 목표 합을 정확하게 만족하면 해당 조합을 결과에 추가함
        if target == 0: 
            ret.append(path)
            return 
         # 후보 숫자들을 하나씩 반복하면서 재귀 호출을 통해 다음 후보 숫자를 고려하여 조합을 찾음.
        for i in range(len(nums)): 
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret) 
