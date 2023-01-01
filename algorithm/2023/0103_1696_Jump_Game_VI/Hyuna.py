class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        # 0번 인덱스 수에서 시작하므로 전체 합을 0번 인덱스 값으로 시작
        # i 는 인덱스를 위한 변수, 0번 인덱스는 더해졌으므로 그 다음인 1로 지정 
        mSum = nums[0]
        i = 1 
        n = len(nums)

        # startIndex에서 k 범위에 해당하는 수들 중 최대값을 찾아 해당 값과 인덱스를 리턴하는 함수 
        def findMax(startIndex):
            maxNum = max(nums[startIndex: min(n, startIndex + k)])
            index = nums[startIndex: min(n, startIndex + k)].index(maxNum)
            return index, maxNum

        while True:
            # 인덱스가 최대 길이보다 크거나 같으면 멈춤 
            if i >= len(nums):
                break

            # findMax함수를 호출해 범위안에서 가장 큰 값과 그 인덱스를 받아옴 
            index, tempMax = findMax(i)
            # 다음 인덱스부터 범위를 다시 잡아야하므로 1을 더해줌 
            i += (index + 1)
            # 최대값을 만들기 위해 범위에서 가장 컷던 값을 더함 
            mSum += tempMax
            
      
        return mSum

