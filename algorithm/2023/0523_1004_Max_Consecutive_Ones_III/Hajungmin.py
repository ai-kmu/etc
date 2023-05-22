class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 윈도우의 가장 왼쪽 인덱스와 0의 개수 초기화
        left = 0  
        zeros = 0  
        # 최대로 나타낼 수 있는 1의 개수
        max_length = 0 
    
        for right in range(len(nums)):  
            # 오른쪽을 의미하는 인덱스를 반복하며 0인 경우 zeros에 1을 더함
            if nums[right] == 0: 
                zeros += 1  
            
            # 만약 zeros가 사용할 수 있는 k개수를 넘었을 경우
            # zeros가 k보다 작아질 때까지 left를 오른쪽으로 옮겨가며 0일 때
            # zeros를 감소시킴
            while zeros > k:
                if nums[left] == 0:  
                    zeros -= 1  
                left += 1 
        
            # 이렇게 생성한 right와 left에 1을 더한 길이와
            # max_length을 비교해 최대값 갱신
            max_length = max(max_length, right - left + 1)  
        
        return max_length  
