class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        # 변수 정의
        n = len(nums)
        # modulo 
        MOD = 10 ** 9 + 7  
        
        # pairs가 없는 경우
        if n<=1:
            return 0
        
        # 역수를 계산하는 함수 ex) rev(42) -> 24
        def reverse(i):
            new = 0
            while(i!= 0):
                r = i % 10
                new = new * 10 + r
                i = i // 10
            return new
        
        # 각 차이의 빈도를 계산
        freq_counter = defaultdict(int)
        for num in nums:
            freq_counter[num - reverse(num)] += 1
        
        # 모든 빈도에 대한 pair 수 계산, nC2 (n choose 2) -> n*(n-1)/2
        answer = 0
        for freq in freq_counter.keys():
            count = freq_counter[freq]
            
            # answer에 계산값 저장
            answer = (answer + (count * (count - 1)) // 2) % MOD
                          
        return answer
