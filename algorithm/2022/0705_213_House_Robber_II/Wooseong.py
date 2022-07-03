'''
DP (memoization)
1. 분할: 해당 집을 훔친다(include) / 안 훔친다(exclude)
2. 반복: 충분히 긴 nums를 생각하면 중간 부분이 여러 번 계산 됨
'''
class Solution:
    '''nums에서 left부터 right까지의 부분을 놓고 봤을 때'''
    def help(self, left, right):
        '''
        base case
        * 현재는 0번과 -1번이 이웃이 아님
        1. left > right는 안됨 -> return 0
        2. (right - left) <= 1 : 여기선 하나 밖에 못 턺 -> return max(nums)
        * nums가 4개, 5개, 6개일 땐 각각 케이스가 3, 5, 11개 나오긴 하는데
          여기까지 하는 건 too much
        '''
        if left > right:
            return 0
        elif (right - left) <= 1:
            return max(self.nums[left:right+1])
        
        '''memoization: 있으면 그거 return'''
        if (left, right) in self.memo:
            return self.memo[(left, right)]
        
        '''left(0)번째 집을 훔치는 경우'''
        include_left = self.nums[left] + self.help(left + 2, right)
        '''left(0)번째 집을 안 훔치는 경우'''
        exclude_left = self.help(left + 1, right)
        
        '''memo하고 return'''
        self.memo[(left, right)] = max(include_left, exclude_left)
        
        return self.memo[(left, right)]
        
    
    def rob(self, nums):
        '''예외 처리: 3개 이하의 집들에선 하나 밖에 못 턺'''
        n = len(nums)
        if n <= 3:
            return max(nums)
        
        '''DP를 위한 self 변수 지정'''
        self.nums = nums
        self.memo = {}
        
        '''0번째 집을 훔치는 경우'''
        include = nums[0] + self.help(2, n-2)
        '''0번째 집을 안 훔치는 경우'''
        exclude = self.help(1, n-1)
        
        '''둘 중 최댓값 반환'''
        return max(include, exclude)
