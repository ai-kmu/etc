class Solution:
    def numberOfSubarrays(self, nums: list, k: int) -> int:
        '''
        input : 
            nums : 
                list of int, 
                e.g. [1,1,2,1,1]
            k : 
                int, 
                e.g. 3
        output : 
            self.answer :  
                int, 
                number of nice sub-arrays
        '''
        self.nums = nums    
        self.k = k
        self.build_up() # build odds_index 
        self.ans = 0 
        self.find_subarray() 
        return self.ans
        
    def build_up(self):
        '''
        nums의 홀 수인 요소 index 저장
        + 이후 사용을 위해 nums의 길이도 저장
        '''
        self.odds_index = []
        for i, num in enumerate(self.nums):
            if num%2 == 1:
                self.odds_index.append(i) 
        self.odds_index.append(len(self.nums))
                
    def find_subarray(self):
        '''
        input : 
            self.nums,
            self.odds_index,
            self.k
        output :
            self.ans
        
        홀 수 사이에 있는 짝 수는 연속하는 홀 수의 개수에 영향을 주지 않으므로 배제함    
        -> 홀 수 index를 저장한 self.odds_index 
            -> 홀 수의 정보만 있음
            -> 이 중 k개를 고르면 연속하는 홀 수 k개를 고른 것임
                -> self.nums : [1,1,2,1,1], self.odds_index : [0, 1, 3, 4, 5], self.k : 3
                -> 이 중 연속하는 3개를 고르면 [0, 1, 3], [1, 3, 4] 나옴 (self.odds_index 기준)
                    -> 이를 self.nums 기준으로 보면 [1,1,2,1], [1,2,1,1] 나옴
                        -> 이 때, 위의 subarray 기준 각 좌측과 우측에 짝수가 있어도 연속하는 홀 수의 개수에는 영향을 주지 않음
                            -> 계산하여 합함
        
        '''
        for i, odd_index in enumerate(self.odds_index[:-1]): # 마지막 index는 num의 길이이므로 배제
            if i+self.k > len(self.odds_index[:-1]): # 현재 index에서 k개를 고를 수 없다면 함수 종료
                return
            
            # 현재 subarray 기준 좌측 판단
            if i == 0: # 계산할 이전 index가 없다면 이전 모든 짝수 개 수 + 현재 자신(+1)
                left = self.odds_index[i] + 1
            else: # 현재 홀 수 index - 이전 홀 수 index -> 홀 수 사이에 있는 짝 수의 수 + 현재 자신
                left = self.odds_index[i] - self.odds_index[i-1] 
            
            # 현재 subarray 기준 우측 판단
            if self.odds_index[i+self.k-1] == len(self.nums): # 선택한 연속하는 뒤 k번째 요소가 마지막 index라면 -> 현재 자신(1)
                right = 1
            else: # 현재 k번째 뒤 홀 수 index - 그 이전 홀 수 index -> 홀 수 사이에 있는 짝 수의 수 + 현재 자신  
                right = self.odds_index[i+self.k] - self.odds_index[i+self.k-1] 

            self.ans += left * right
