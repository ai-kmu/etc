class Solution(object):
    def threeSumClosest(self, nums, target):

        nums.sort()

        answer=0
        for i in nums[:3]:
            answer+=i

        #answer와 target숫자간의 차이 계산
        md = answer - target
        nums_len = len(nums)

        for i in range(nums_len - 2):
            leftNum, rightNum = i + 1, nums_len - 1
            small = nums[i] + nums[leftNum] + nums[leftNum + 1]
            big = nums[i] + nums[rightNum] + nums[rightNum - 1]

            if small > target: # 만약 가장 작은 수의 합들이 target보다 크면
                md = min(md, small - target, key=abs)
            elif big < target: # 만약 가장 큰 수의 합들이 target보다 작으면
                md = min(md, big - target, key=abs)
            else: # target보다 작은 것이 없으면
                while leftNum < rightNum:  #왼쪽수가 오른쪽수보다 같거나 커지지 않을 때까지 반복
                    sum = nums[i] + nums[leftNum] + nums[rightNum]
                    if sum < target:
                        leftNum += 1
                    elif sum > target:
                        rightNum -= 1
                    else:
                        return target
                    md = min(md, sum - target, key=abs)

        return target + md




if __name__ == '__main__':
    nums=[0,2,1,-3]
    target=1
    s=Solution()
    print(s.threeSumClosest(nums,target))