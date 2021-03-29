class Solution:
    def jump(self, nums: List[int]) -> int:
        
        # maxJum는  최대 이동할 수 있는 인덱스
        # tempInd는 최대 이동 가능 인덱스에 탐색중인 인덱스가 도달하면,maxInd로 갱신
        tempInd, maxInd, step = 0, 0, 0
        for i in range(len(nums)-1):
            maxInd = max(nums[i] + i, maxInd)
            if tempInd == i:
                tempInd = maxInd
                step += 1

        return step
