class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        self.dict = dict()  # nums 값 저장 
        for i in nums:
            self.dict[i] = True
        self.n_bit = len(nums[0])  # 고려해야 할 bit 수
        self.ans = None
        self.dfs("")
        return self.ans
    
    def dfs(self, cur_num):
        if self.ans is not None:  # 정답값이 저장되었다면 함수 종료
            return 
        if len(cur_num) == self.n_bit:  
            try: 
                self.dict[cur_num]  
            except:  # unique binary string 이라면 정답값 저장
                self.ans = cur_num 
        else:
            self.dfs(cur_num + '0')
            self.dfs(cur_num + '1')
        
